---
hidden: true
icon: lock
---

# Security Model

### **1. Introduction** <a href="#id-1-introduction" id="id-1-introduction"></a>

Jibril is a next-generation runtime security tool designed to monitor and detect anomalies in system behavior with precision, efficiency, and minimal system overhead. By leveraging the power of eBPF (extended Berkeley Packet Filter), Jibril collects and stores behavioral data directly within the kernel using key-value maps. This innovative approach enables advanced detections through a secure, query-driven model, ensuring high performance and reliability even in high-throughput environments. Unlike traditional security tools that rely on event-streaming mechanisms, Jibril's architecture avoids potential bottlenecks and latency issues, providing a robust solution for modern runtime security challenges.

This document outlines Jibril's comprehensive security model, detailing its architecture, data handling mechanisms, plugin and extension designs, and compliance measures. It provides an in-depth explanation of how Jibril safeguards data integrity, enforces trust boundaries, and aligns with privacy and security best practices. The document also highlights Jibril's extensibility, resilience, and future enhancement roadmap, offering readers a thorough understanding of the principles, mechanisms, and safeguards that make Jibril a robust and adaptable solution for runtime security.

### **2. Security Principles** <a href="#id-2-security-principles" id="id-2-security-principles"></a>

Jibril's security model is built upon core principles that emphasize safeguarding data integrity, ensuring operational transparency, and enhancing resilience against potential tampering or attacks. These principles guide the design and implementation of Jibril's features and are crucial for maintaining a secure and trustworthy system.

#### **2.1 Behavioral Data Integrity** <a href="#id-21-behavioral-data-integrity" id="id-21-behavioral-data-integrity"></a>

* **Detection Recipe Privacy**: Jibril ensures that detection recipes, which define the patterns and behaviors to be monitored, are private and accessible only to authorized users. This privacy is critical because if malicious actors were aware of the specific detection patterns, they could potentially craft methods to bypass the detection mechanisms. By keeping these recipes confidential, Jibril maintains the effectiveness of its monitoring capabilities.
* **Rate-Limiting on Repetitive Events**: To prevent the system from being overwhelmed by repetitive events, Jibril implements rate-limiting mechanisms within its detection recipes. These limits can be applied per process, per binary, or globally, controlling the number of events generated within a specific time frame. This approach reduces unnecessary overhead and helps maintain system performance without compromising the effectiveness of monitoring.
* **Key-Value Data-Store Architecture**: Jibril stores behavioral data in eBPF maps within the kernel. These maps use hashed keys that function similarly to foreign keys in a relational database, enabling robust data linkage across different maps (e.g., linking tasks to commands or binaries to files). Root users can inspect the map formats and use these keys to link data, but they cannot generate or modify the keys themselves, ensuring the integrity and consistency of the collected data.
* **Mutable Data with Traceability**: Privileged users can read and change eBPF map values, but such modifications would not go unnoticed, thereby tainting the environment. The key is hashed, and any attempt to create a new hash would likely break the relationship between the data and its metadata, ensuring the integrity of the collected data.

#### **2.2 Kernel/Userland Separation** <a href="#id-22-kerneluserland-separation" id="id-22-kerneluserland-separation"></a>

* **Detection Layers**: Jibril's architecture separates detection responsibilities between kernel space and userland. The kernel-space operations focus on securely storing behavioral data with minimal interaction required between the kernel and userland. Primary detections, such as pattern matching and data analysis, are conducted in userland using the cached data retrieved from the kernel. This separation enhances security and reduces the risk of kernel-level vulnerabilities.
* **Event-Free Design**: Unlike traditional runtime security tools that rely on streaming events from the kernel to userland, Jibril employs a query-driven model. This design choice eliminates the risk of overload attacks that can delay detection and ensures a timely response to incidents without introducing additional latency. By avoiding event-streaming mechanisms, Jibril reduces overhead and improves performance in high-throughput environments.

#### **2.3 Access Control and Monitoring** <a href="#id-23-access-control-and-monitoring" id="id-23-access-control-and-monitoring"></a>

* **Kernel Access**: Access to eBPF maps and programs is restricted to root users with specific capabilities. While these users can inspect the map formats and query the stored data, they cannot directly generate the hashed keys or modify the data within the maps. Unauthorized actions, such as writing to eBPF maps, loading unverified eBPF programs, or installing kernel modules, are detected and flagged as environmental tampering events. This strict access control prevents unauthorized modifications and maintains the integrity of the monitoring system.
* **Userland Privilege Management**: The userland component of Jibril currently runs with root privileges and the `CAP_BPF` capability (supported in kernel versions 5.8 and later, or `CAP_SYS_ADMIN` capability in earlier kernels) to query eBPF maps and perform initialization tasks. In future releases, Jibril will drop unnecessary capabilities after initialization, adhering to the principle of least privilege. This approach reduces the risk of misuse or privilege escalation, enhancing the overall security of the system.

#### **2.4 System Resilience** <a href="#id-24-system-resilience" id="id-24-system-resilience"></a>

* **Environmental Tamper Detection**: Jibril actively monitors for actions that could compromise its integrity. These actions include unauthorized writes to eBPF maps, loading or unloading of rogue eBPF programs, and the installation or removal of kernel modules. When such events are detected, they are logged and flagged as environmental taints, alerting administrators to potential tampering or malicious activities.
* **Fault Isolation**: The tool's modular architecture ensures that faults or issues within plugins or extensions do not compromise the core system. Each plugin operates in isolation, typically within its own thread, so if one plugin encounters a problem, such as a crash or infinite loop, other plugins and the core system continue to function unaffected. This design enhances the resilience and stability of Jibril, ensuring continuous monitoring even in the presence of component failures.

#### **2.5 Alignment with Compliance Standards** <a href="#id-25-alignment-with-compliance-standards" id="id-25-alignment-with-compliance-standards"></a>

Jibril is designed with flexibility to align with privacy and security standards such as the General Data Protection Regulation (GDPR) and ISO 27001. While the specifics of compliance depend on deployment requirements, Jibril incorporates features and practices that support adherence to these standards.

* **GDPR Compliance**: Jibril collects metadata about file access, including filenames, types of access, processes accessing the files, and timestamps. It does not currently monitor file contents, which reduces concerns related to personal data processing under GDPR. However, if future enhancements introduce monitoring of file contents, Jibril will implement anonymization or obtain explicit justification for processing sensitive data to ensure GDPR compliance.
* **ISO 27001 Alignment**: Although Jibril is not currently deployed in environments requiring formal ISO 27001 certification, its robust logging, access control mechanisms, and tamper-detection features provide a strong foundation for aligning with the standard's requirements. Future considerations may include formal documentation of security risks, processes, and monitoring practices to support certification efforts.

### **3. System Architecture and Trust Boundaries** <a href="#id-3-system-architecture-and-trust-boundaries" id="id-3-system-architecture-and-trust-boundaries"></a>

Jibril's architecture is designed to maintain clear separation between components, enforce trust boundaries, and ensure secure data handling throughout the system. The architecture consists of two main components: the eBPF loader operating in kernel space and the userland daemon operating in user space. This section details the responsibilities and security mechanisms of each component, as well as the trust boundaries between them.

#### **3.1 eBPF Loader (Kernel Space)** <a href="#id-31-ebpf-loader-kernel-space" id="id-31-ebpf-loader-kernel-space"></a>

**Responsibilities**:

* **Deployment of eBPF Programs**: The eBPF loader deploys eBPF programs that monitor system behavior, track relevant events, and collect data securely within the kernel.
* **In-Kernel Data Storage**: It provides in-kernel data storage using eBPF maps, which act as key-value stores accessible by both kernel and authorized userland processes.

**Security Mechanisms**:

**eBPF Safety Characteristics**:

* **Kernel Verifier Enforcement**: eBPF programs are verified by the Linux kernel's eBPF verifier before they are loaded. This verification ensures that the programs cannot perform unsafe operations, access unauthorized memory, or corrupt the kernel, providing a layer of safety not present with traditional kernel modules.
* **Safety over Kernel Modules**: Unlike kernel modules, which can introduce kernel-level vulnerabilities and destabilize the system, eBPF programs run in a restricted environment with enforced safety checks, making them a secure alternative for kernel-space operations.
* **Userland Map Access Control**:
  * **Restricted Access**: Access to eBPF maps is restricted to root users with specific capabilities, such as `CAP_BPF`. Unauthorized users or processes cannot interact with these maps, preventing unauthorized access or tampering.
  * **Mutable Data with Traceability**: While privileged users can query and modify the eBPF maps to retrieve and change data, such modifications would not go unnoticed, thereby tainting the environment. The key is hashed, and any attempt to create a new hash would likely break the relationship between the data and its metadata, ensuring the integrity of the collected data.
* **Memory Safety**:
  * **Bounds Checking**: eBPF programs adhere to strict bounds checking and constraints enforced by the verifier. This prevents unsafe memory operations, such as buffer overflows or invalid memory access, within the kernel.
* **Tamper Detection**:
  * **Monitoring Unauthorized Actions**: Jibril detects and logs unauthorized actions, such as attempts to write to eBPF maps, load unverified eBPF programs, or install kernel modules. These events are flagged as environmental tampering and can trigger alerts or additional security responses.

#### **3.2 Uniform Binary Object Across Kernel Versions** <a href="#id-32-uniform-binary-object-across-kernel-versions" id="id-32-uniform-binary-object-across-kernel-versions"></a>

eBPF programs run the same binary object across different kernel versions, ensuring consistency and compatibility regardless of the kernel version they are running on.

Benefits:

* **Simplified Deployment**: There is no need to maintain different versions or builds of eBPF programs for different kernel versions, simplifying the deployment process.
* **Consistency**: Running the same binary object ensures consistent behavior and performance across various environments.
* **Reduced Maintenance**: With a single binary object, maintenance efforts are reduced as there is no need to test and validate multiple versions.
* **Enhanced Compatibility**: Ensures compatibility with a wide range of kernel versions, reducing the risk of version-specific issues or bugs.

#### **3.3 Userland Daemon (User Space)** <a href="#id-33-userland-daemon-user-space" id="id-33-userland-daemon-user-space"></a>

**Responsibilities**:

* **Data Analysis and Detection**:
  * **Pattern Matching**: The userland daemon performs pattern matching and data analysis on the behavioral data retrieved from the eBPF maps. This allows for the detection of anomalies or suspicious activities based on predefined detection recipes.
  * **Cached Data Utilization**: It utilizes cached data to enhance performance and reduce the need for frequent kernel-userland interactions.
* **Plugin and Printer Management**:
  * **Plugin Execution**: The daemon manages plugins, which extend the detection capabilities of Jibril. Plugins run in separate threads, each with their own dispatching logic, allowing for modular and efficient execution.
  * **Event Dispatching**: It handles the dispatching of detection events to configured endpoints through printers, which can include standard output, files, dashboards, or other systems.

**Security Mechanisms**:

* **Access Control and Privilege Management**:
  * **Limited Capabilities**: The daemon runs with the minimum required privileges. After initialization tasks that require higher privileges (such as querying eBPF maps), unnecessary capabilities are dropped in adherence to the principle of least privilege.
  * **Configuration-Based Restrictions**: Access to sensitive APIs and plugins is restricted based on configurations and user permissions, preventing unauthorized use or modification.
* **Thread-Based Isolation**:
  * **Plugin Isolation**: Each plugin operates in its own thread or set of threads, providing execution isolation. If a plugin encounters an issue, such as a crash or infinite loop, it does not affect other plugins or the core daemon, enhancing the resilience of the system.
* **Endpoint Authentication and Secure Communication**:
  * **Authenticated Endpoints**: Printers dispatch data only to pre-configured, authorized endpoints. For example, the `listen.dev` dashboard accepts data submitted with specific API keys, ensuring that only authorized data submissions are processed.
  * **Data Sanitization**: Before data is submitted to endpoints, it undergoes strict validation and sanitization to prevent injection attacks or the transmission of malformed data.

#### **3.4 Trust Boundaries** <a href="#id-34-trust-boundaries" id="id-34-trust-boundaries"></a>

* **Kernel/User Space Separation**:
  * **Data Integrity Across Boundaries**: The kernel-space component (eBPF loader and maps) and the user-space daemon maintain a clear separation of responsibilities and data handling. The kernel securely collects and stores data, while the user-space daemon performs analysis without modifying collected data kernel state.
  * **Secure Data Retrieval**: The user-space daemon retrieves data from the eBPF maps using secure, authorized methods. Direct manipulation of kernel data structures from user space - from other processes - is not permitted, preserving data stability and security.
* **Plugin and Printer Isolation**:
  * **Scoped Permissions**: Plugins and printers operate within defined scopes and permissions, ensuring they cannot perform unauthorized actions or access restricted data.
  * **Inter-Component Communication**: Communication between plugins, printers, and the core daemon is controlled and monitored, preventing unauthorized data flows or interference.

### **4. Data Handling, Security, and Threat Mitigation** <a href="#id-4-data-handling-security-and-threat-mitigation" id="id-4-data-handling-security-and-threat-mitigation"></a>

Jibril's data handling approach is designed to address the challenges of high-throughput, real-time security monitoring while ensuring data security and integrity. By employing a query-driven model and storing data within the kernel, Jibril avoids common pitfalls associated with traditional event-streaming mechanisms.

#### **4.1 Data Storage (Kernel Space)** <a href="#id-41-data-storage-kernel-space" id="id-41-data-storage-kernel-space"></a>

* **In-Kernel Hashmaps**:
  * **Key-Value Stores**: Jibril uses eBPF hashmaps as key-value stores to collect and store behavioral data securely within the kernel. These maps efficiently manage data such as events, metrics, and state information.
  * **Hashed Keys**: Keys used in the hashmaps are hashed, serving as a security measure to prevent unauthorized key generation or prediction. This hashing also enhances data retrieval efficiency.
* **Data Characteristics**:
  * **No Encryption, But Hashed**: Data within the eBPF maps is not encrypted, but sensitive identifiers are hashed to obscure raw values. This approach balances performance considerations with security needs.
  * **Immutability and Overwriting**: Once data is stored in the eBPF maps, it is immutable from the perspective of user space. New data can overwrite old entries as updates occur, ensuring that the maps contain current information without growing indefinitely.
* **Garbage Collection and Resource Management**:
  * **Automatic Overwriting**: eBPF maps have finite sizes. When they reach capacity, old or less relevant data is automatically overwritten by new entries, preventing resource exhaustion.
  * **Tamper Detection**: Any unauthorized attempts to modify the eBPF maps are detectable through Jibril's tamper-detection mechanisms, ensuring data integrity.

#### **4.2 Data Movement** <a href="#id-42-data-movement" id="id-42-data-movement"></a>

* **Query-Driven Model**:
  * **On-Demand Data Retrieval**: Instead of pushing data from the kernel to userland through event streams, Jibril allows the user-space daemon to retrieve data from eBPF maps on demand. This approach reduces the overhead associated with constant event streaming and minimizes the risk of data loss.
  * **Elimination of Bottlenecks**: By avoiding producer-consumer mismatches inherent in event-driven pipelines, Jibril ensures that high event rates in the kernel do not overwhelm the user-space daemon, enhancing system stability and performance.
* **High-Performance Design**:
  * **Reduced Data Copying**: The query model reduces unnecessary data copying between kernel and user space, as only relevant data is retrieved when needed.
  * **Efficient Data Access**: Tailored queries allow for efficient access to specific data sets, reducing the volume of data transferred and processed.

#### **4.3 Data Querying** <a href="#id-43-data-querying" id="id-43-data-querying"></a>

* **Flexible Query Model**:
  * **Detection Logic-Driven Queries**: The user-space daemon employs a flexible query model driven by detection logic and user-defined patterns. This allows for precise and efficient data retrieval from the eBPF maps.
* **Filtering and Enrichment**:
  * **In-Kernel Filtering**: Basic filtering can occur during query execution to minimize unnecessary data retrieval.
  * **User-Space Enrichment**: Data enrichment and comprehensive analysis are performed in user space, leveraging more abundant resources and avoiding the constraints of kernel-space operations.
* **Access Control**:
  * **Authorized Queries**: Only authorized processes with the necessary privileges can perform queries on the eBPF maps, ensuring that data access is controlled and monitored.

### **5. Extensions & Plugins Security** <a href="#id-5-extensions-plugins-security" id="id-5-extensions-plugins-security"></a>

Plugins and extensions are essential for extending Jibril's detection capabilities and integrating with various systems. Their design prioritizes security, stability, and maintainability.

#### **5.1 Plugins** <a href="#id-51-plugins" id="id-51-plugins"></a>

* **Built-In Design**:
  * **Compile-Time Extension**: Plugins are built into Jibril at compile time by incorporating detection recipes into the codebase. This approach ensures stability by avoiding the risks associated with runtime extensibility, such as compatibility issues or unforeseen errors.
  * **Future Extensibility**: While runtime extensibility is planned for future releases—potentially through descriptive languages for defining detection logic—the current model emphasizes reliability and control.
* **Grouped by Detection Mechanisms**:
  * **Organization**: Plugins are organized based on specific detection mechanisms, such as file access events, execution patterns, or network flows. This organization promotes code reuse and consistency across plugins.
  * **Shared Logic**: Common logic is shared among plugins within the same group, reducing redundancy and potential errors.
* **Thread-Based Isolation**:
  * **Separate Execution Threads**: Each plugin operates in its own thread or set of threads. This isolation ensures that if one plugin experiences an issue, it does not impact the operation of others or the core system.
  * **Resilience**: This design enhances system resilience, as faults are contained within individual plugins.
* **Maintainability and Resilience**:
  * **Modular Codebase**: The modular architecture simplifies maintenance and allows for easier updates or additions of detection capabilities.
  * **Fault Tolerance**: The system's resilience to plugin failures ensures continuous monitoring and detection capabilities.

#### **5.2 Printers** <a href="#id-52-printers" id="id-52-printers"></a>

* **Built-In Mechanism**:
  * **Predefined Dispatch Methods**: Printers are built-in components responsible for dispatching detection events to various endpoints. They are not extendable at runtime, ensuring predictable behavior and reducing the risk of runtime errors.
  * **Configuration-Based Enabling**: Printers can be enabled or disabled through configuration files, providing flexibility in how events are dispatched without altering the codebase.
* **Customizability for Specific Needs**:
  * **Tailored Printers**: For specific customer requirements, additional printers can be developed to dispatch events to custom endpoints. This allows Jibril to integrate with specialized infrastructure or systems.
* **Endpoint Security**:
  * **Authorized Endpoints**: Printers enforce restrictions to ensure that events are only dispatched to predefined, authorized endpoints.
  * **Data Validation and Sanitization**: Data transmitted by printers is subjected to strict format validation and sanitization processes. This prevents injection attacks and ensures that only well-formed, secure data is sent to endpoints.
  * **Authenticated Channels**: Communication with endpoints utilizes authenticated channels, such as APIs secured with tokens or keys, to protect data integrity and confidentiality.

### **6. Compliance Measures** <a href="#id-6-compliance-measures" id="id-6-compliance-measures"></a>

Jibril incorporates measures to ensure compliance with data protection regulations and industry standards, focusing on data privacy, security of submitted data, auditing, and regulatory alignment.

#### **6.1 Data Privacy** <a href="#id-61-data-privacy" id="id-61-data-privacy"></a>

* **Strict Data Collection Policies**:
  * **Minimal Data Collection**: Jibril collects only the metadata necessary for effective monitoring and detection. This includes information like file paths, process identifiers, and network flow details, avoiding the collection of unnecessary or sensitive personal data.
* **Event Submission Control**:
  * **Configurable Printers**: The destination of detection events is controlled by the enabled printers. Options include standard output, file logging, the `listen.dev` dashboard, and optional integrations with OpenAI services.
* **OpenAI Plugins**:
  * **Summarization of Events**: For enhanced analysis, Jibril can utilize OpenAI plugins to summarize detection events. These summaries provide concise insights into changes, network flows, and detections without exposing raw data.
  * **Data Protection**: Events submitted to OpenAI are minimal and authenticated. Temporary files created during the summarization process are ephemeral and deleted after use, ensuring that no persistent or sensitive data is stored externally.
* **Data Anonymization**:
  * **Future Implementation**: While anonymization features are not currently implemented, they are planned for future releases. These features will further enhance privacy protections by obscuring personal identifiers in the collected data.
* **Data Encryption**:
  * **Planned Enhancements**: Future updates may include encryption of data within kernel space and user space, particularly for deployments requiring heightened security measures.

#### **6.2 Security of Submitted Data** <a href="#id-62-security-of-submitted-data" id="id-62-security-of-submitted-data"></a>

* **API Authentication**:
  * **Secure Submissions**: Detection events sent to external systems, such as the `listen.dev` dashboard or OpenAI services, are protected by strong authentication mechanisms. This includes the use of API keys or tokens, ensuring that only authorized data is accepted.
* **Secure Transmission**:
  * **Encrypted Channels**: Data is transmitted over secure channels, such as HTTPS, to prevent interception or tampering during transmission.
* **Data Minimization**:
  * **Limited Data Exposure**: Only essential information is included in submissions to external systems, reducing the risk associated with data leakage.

#### **6.3 Auditing and Logging** <a href="#id-63-auditing-and-logging" id="id-63-auditing-and-logging"></a>

* **Comprehensive Audit Logs**:
  * **Detailed Logging**: Jibril maintains detailed logs of actions, events, and detections. These logs provide a robust audit trail that can be used for compliance verification, forensic analysis, or troubleshooting.
* **Trace Mode**:
  * **Enhanced Observability**: An optional TRACE mode provides detailed observability of Jibril's operations, including function names, package names, and line numbers.
  * **Controlled Activation**: TRACE mode is disabled by default and must be explicitly enabled, preventing unnecessary exposure of internal operations.

#### **6.4 External Data Store Integration** <a href="#id-64-external-data-store-integration" id="id-64-external-data-store-integration"></a>

* **Scalability and Security**:
  * **Kafka-Backed Dashboards**: Integration with systems like the `listen.dev` dashboard, which is backed by Kafka, allows for scalable and efficient handling of detection events.
  * **Secure Integrations**: Data sent to external systems is secured through authenticated APIs, ensuring that integrations do not compromise data integrity or security.

#### **6.5 GDPR and Regulatory Alignment** <a href="#id-65-gdpr-and-regulatory-alignment" id="id-65-gdpr-and-regulatory-alignment"></a>

* **GDPR Compliance**:
  * **Data Protection Principles**: Jibril's data collection practices align with GDPR principles by minimizing data collection and avoiding personal data where possible.
  * **Anonymization and Justification**: Future features will include data anonymization, and any processing of sensitive data will be justified and documented to comply with GDPR requirements.
* **ISO 27001 Considerations**:
  * **Strong Security Foundation**: Jibril's security mechanisms, including access control, tamper detection, and comprehensive logging, provide a strong foundation for alignment with ISO 27001 standards.
  * **Future Certification**: Formal documentation and processes can be developed to pursue ISO 27001 certification if required by deployment environments.

### **7. Summary** <a href="#id-7-summary" id="id-7-summary"></a>

Jibril is a state-of-the-art runtime security tool that leverages the power of eBPF to deliver precise and efficient behavioral monitoring without compromising system performance. By employing a query-driven model and avoiding traditional event-streaming mechanisms, Jibril minimizes data loss and reduces the overhead associated with high-throughput, real-time contexts.

Its modular design integrates built-in plugins grouped by detection mechanisms, ensuring maintainability, resilience, and fault isolation. Printers enable flexible event dispatch to secure endpoints, including the `listen.dev` dashboard and optional OpenAI-powered summaries. Jibril's architecture balances operational transparency, security, and adaptability, making it a trusted solution for modern runtime security needs.

Current features focus on data integrity, strict access control, and robust authentication mechanisms. Future enhancements will introduce data anonymization and encryption, aligning the tool further with GDPR and ISO 27001 standards.

Jibril's comprehensive security model addresses key threats and challenges in runtime security, providing organizations with a robust and adaptable solution for protecting their systems.
