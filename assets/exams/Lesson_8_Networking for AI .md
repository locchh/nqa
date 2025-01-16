# Networking for AI

### General Concepts

**1. What are the four networks typically found in an AI data center?**

A. Compute, storage, management, and user networks  
B. Internal, external, wireless, and wired networks  
C. Public, private, hybrid, and community networks  
D. VPN, LAN, WAN, and SAN  

**Answer:** A. Compute, storage, management, and user networks  

---

**2. What is the primary function of the compute network in an AI data center?**

A. To manage storage devices  
B. To connect compute nodes and facilitate data processing  
C. To monitor power consumption  
D. To provide internet access  

**Answer:** B. To connect compute nodes and facilitate data processing  

---

**3. How does the storage network enhance performance in AI workloads?**

A. By increasing latency  
B. By providing faster access to data and optimizing data transfer rates  
C. By limiting the amount of data stored  
D. By reducing the number of storage devices  

**Answer:** B. By providing faster access to data and optimizing data transfer rates  

---

**4. What role does the in-band management network serve in a data center?**

A. It is used for data transfer only  
B. It manages server operations and monitors performance through the same channels as data traffic  
C. It connects external networks only  
D. It provides backup for data storage  

**Answer:** B. It manages server operations and monitors performance through the same channels as data traffic  

---

**5. How does an out-of-band management network differ from an in-band management network?**

A. Out-of-band networks cannot connect to servers  
B. Out-of-band networks operate on separate channels, allowing management without affecting data traffic  
C. In-band networks are faster  
D. Out-of-band networks are more expensive  

**Answer:** B. Out-of-band networks operate on separate channels, allowing management without affecting data traffic  

---

### Networking Requirements

**6. Why is high bandwidth important for GPU-based systems?**

A. It reduces costs  
B. It allows for faster data transfer, enabling efficient processing of large datasets  
C. It minimizes the number of GPUs needed  
D. It eliminates the need for cooling  

**Answer:** B. It allows for faster data transfer, enabling efficient processing of large datasets  

---

**7. How does GPU utilization impact performance in AI workloads?**

A. Higher GPU utilization leads to decreased performance  
B. Low GPU utilization improves performance  
C. Higher GPU utilization typically results in better performance and faster processing of AI tasks  
D. GPU utilization has no impact on performance  

**Answer:** C. Higher GPU utilization typically results in better performance and faster processing of AI tasks  

---

**8. What factors influence the performance of AI models on GPU systems?**

A. Only the number of GPUs  
B. Data transfer speed, GPU memory, and model complexity  
C. The age of the hardware  
D. The operating system only  

**Answer:** B. Data transfer speed, GPU memory, and model complexity  

---

**9. What are the key networking factors that affect performance in AI data centers?**

A. Weather conditions  
B. Latency, bandwidth, and jitter  
C. Number of physical servers  
D. Distance from the cloud  

**Answer:** B. Latency, bandwidth, and jitter  

---

**10. Why is it important to minimize GPU idle time in AI workloads?**

A. Idle GPUs consume more power  
B. Reducing idle time maximizes resource utilization and improves overall throughput  
C. Idle GPUs have no effect on performance  
D. Idle time is only a concern for CPU workloads  

**Answer:** B. Reducing idle time maximizes resource utilization and improves overall throughput  

---

### Traditional vs. AI-Optimized Networks

**11. What is the difference between a traditional north-south network and an AI-optimized network?**

A. North-south networks are used only for external communication  
B. AI-optimized networks focus on low latency and high bandwidth for data-intensive tasks, while traditional networks may not  
C. Traditional networks do not support AI applications  
D. There is no difference  

**Answer:** B. AI-optimized networks focus on low latency and high bandwidth for data-intensive tasks, while traditional networks may not  

---

**12. How does the presence of dependencies between nodes affect AI data center performance?**

A. It has no impact  
B. Dependencies can lead to bottlenecks, reducing overall system efficiency  
C. It always improves performance  
D. Dependencies simplify data processing  

**Answer:** B. Dependencies can lead to bottlenecks, reducing overall system efficiency  

---

**13. Why is low latency crucial in AI-optimized networks?**

A. It increases the cost of operations  
B. Low latency is essential for real-time data processing and quick response times in AI applications  
C. It has no significance in AI workloads  
D. It only matters in cloud environments  

**Answer:** B. Low latency is essential for real-time data processing and quick response times in AI applications  

---

**14. What are the implications of high jitter in traditional networks for AI applications?**

A. It ensures consistent data flow  
B. High jitter can cause delays and inconsistent data transfer, negatively impacting performance  
C. It has no effect on AI applications  
D. High jitter always improves performance  

**Answer:** B. High jitter can cause delays and inconsistent data transfer, negatively impacting performance  

---

**15. How do AI factories differ from AI clouds in terms of networking requirements?**

A. AI factories require less bandwidth  
B. AI factories often have more stringent latency and bandwidth requirements due to localized processing needs compared to AI clouds  
C. There is no difference in requirements  
D. AI clouds need more physical servers  

**Answer:** B. AI factories often have more stringent latency and bandwidth requirements due to localized processing needs compared to AI clouds  

---

### InfiniBand Overview

**16. What is InfiniBand, and what are its key features?**

A. A type of software application  
B. A high-speed network architecture that offers low latency, high throughput, and supports remote direct memory access (RDMA)  
C. An outdated networking technology  
D. A standard for wireless communication  

**Answer:** B. A high-speed network architecture that offers low latency, high throughput, and supports remote direct memory access (RDMA)  

---

**17. How does InfiniBand ensure high throughput and low latency?**

A. By using traditional TCP/IP protocols  
B. By employing specialized hardware and efficient data transfer protocols  
C. By relying solely on software optimization  
D. By increasing the number of network hops  

**Answer:** B. By employing specialized hardware and efficient data transfer protocols  

---

**18. What is the role of RDMA in InfiniBand technology?**

A. It is not relevant to InfiniBand  
B. RDMA allows data to be transferred directly between the memory of two computers without involving the CPU, reducing latency  
C. RDMA slows down data transfer  
D. RDMA only works with Ethernet  

**Answer:** B. RDMA allows data to be transferred directly between the memory of two computers without involving the CPU, reducing latency  

---

**19. How does RDMA improve data transfer efficiency in AI workloads?**

A. By increasing CPU workload  
B. By enabling zero-copy data transfer, reducing latency and CPU overhead  
C. By limiting data access  
D. By using slower protocols  

**Answer:** B. By enabling zero-copy data transfer, reducing latency and CPU overhead  

---

**20. What are the benefits of hardware offloading in InfiniBand network adapters?**

A. It complicates network management  
B. It reduces CPU usage and improves overall system performance by offloading tasks from the CPU to the network adapter  
C. It has no benefits  
D. It increases latency  

**Answer:** B. It reduces CPU usage and improves overall system performance by offloading tasks from the CPU to the network adapter  

---

### Ethernet Overview

**21. When was Ethernet first introduced, and how has it evolved?**

A. 1980; it has remained unchanged  
B. 1973; it has evolved to support higher speeds and different protocols  
C. 1990; it only supports wireless connections  
D. 2000; it is now obsolete  

**Answer:** B. 1973; it has evolved to support higher speeds and different protocols  

---

**22. How does Ethernet's compatibility impact its use in data centers?**

A. It is not compatible with modern technology  
B. Its compatibility with various devices and protocols makes it widely adaptable for different applications in data centers  
C. It can only connect with older systems  
D. Compatibility is irrelevant for data centers  

**Answer:** B. Its compatibility with various devices and protocols makes it widely adaptable for different applications in data centers  

---

**23. What are the advantages of using Ethernet for AI cloud applications?**

A. It limits bandwidth  
B. It provides a cost-effective solution with broad compatibility and scalability for cloud applications  
C. It reduces security  
D. It is primarily used for local applications only  

**Answer:** B. It provides a cost-effective solution with broad compatibility and scalability for cloud applications  

---

**24. What is RDMA over Converged Ethernet (RoCE), and how does it function?**

A. A new version of Ethernet  
B. It allows RDMA functionality to operate over Ethernet networks, improving data transfer efficiency  
C. A standard for wireless connections  
D. It is unrelated to data transfer  

**Answer:** B. It allows RDMA functionality to operate over Ethernet networks, improving data transfer efficiency  

---

**25. How does RoCE enhance data transfer for AI, storage, and big data applications?**

A. By increasing latency during transfers  
B. By allowing RDMA to operate over Ethernet, enabling low-latency, high-throughput data transfer  
C. By limiting the amount of data transferred  
D. By eliminating the need for networking altogether  

**Answer:** B. By allowing RDMA to operate over Ethernet, enabling low-latency, high-throughput data transfer  

---

### GPUDirect RDMA

**26. What is GPUDirect RDMA, and how does it optimize data movement?**

A. A protocol for wireless data transfer  
B. A technology that allows direct memory access between GPUs and network adapters, bypassing the CPU to reduce latency and improve throughput  
C. A type of storage technology  
D. A traditional data transfer method  

**Answer:** B. A technology that allows direct memory access between GPUs and network adapters, bypassing the CPU to reduce latency and improve throughput  

---

**27. How does GPUDirect RDMA reduce CPU utilization in data transfers?**

A. By increasing CPU workload  
B. By allowing data to be transferred directly between devices without CPU intervention  
C. By using more CPU resources  
D. By making data transfers slower  

**Answer:** B. By allowing data to be transferred directly between devices without CPU intervention  

---

**28. What are the main advantages of using GPUDirect RDMA compared to traditional packet flow?**

A. It increases the number of packets processed  
B. It allows for higher bandwidth, lower latency, and reduced CPU overhead  
C. It is less efficient  
D. It requires more complex networking  

**Answer:** B. It allows for higher bandwidth, lower latency, and reduced CPU overhead  

---

**29. How does GPUDirect RDMA improve end-to-end latency?**

A. By slowing down data transfer rates  
B. By reducing the number of hops data must make through the CPU and network stack  
C. By increasing packet size  
D. By using a less efficient protocol  

**Answer:** B. By reducing the number of hops data must make through the CPU and network stack  

---

**30. What is the significance of minimizing PCI transactions in GPUDirect RDMA?**

A. It complicates data transfers  
B. Minimizing PCI transactions helps reduce latency and improve overall data transfer efficiency  
C. It has no impact on performance  
D. It requires more physical connections  

**Answer:** B. Minimizing PCI transactions helps reduce latency and improve overall data transfer efficiency  

---

### NVIDIA Networking Portfolio

**31. What challenges do growing AI workloads present for data centers?**

A. Decreased demand for computing resources  
B. Increased requirements for bandwidth, low latency, and efficient data management  
C. Reduced data storage needs  
D. More straightforward network management  

**Answer:** B. Increased requirements for bandwidth, low latency, and efficient data management  

---

**32. How does NVIDIA address the networking demands of AI workloads?**

A. By using outdated technology  
B. By providing a range of networking solutions, including InfiniBand and Ethernet optimized for AI workloads  
C. By eliminating network requirements  
D. By focusing only on CPU performance  

**Answer:** B. By providing a range of networking solutions, including InfiniBand and Ethernet optimized for AI workloads  

---

**33. What features does the Nvidia ConnectX family of network interface cards provide?**

A. Only standard data transfer capabilities  
B. High bandwidth, low latency, and support for advanced features like RDMA and GPUDirect  
C. Outdated compatibility with older technologies  
D. Limited network monitoring options  

**Answer:** B. High bandwidth, low latency, and support for advanced features like RDMA and GPUDirect  

---

**34. How do BlueField DPUs enhance the performance of AI workloads?**

A. By increasing power consumption  
B. By offloading networking and storage tasks from the CPU, improving overall efficiency  
C. By reducing the number of GPUs needed  
D. By complicating data management  

**Answer:** B. By offloading networking and storage tasks from the CPU, improving overall efficiency  

---

**35. What are the key attributes of the Nvidia Spectrum Ethernet switch family?**

A. Limited speed and performance  
B. High performance, low latency, and support for advanced networking features for data centers  
C. Outdated technology with no improvements  
D. Only suitable for small networks  

**Answer:** B. High performance, low latency, and support for advanced networking features for data centers  

---

### Spectrum-X and AI Data Centers

**36. What is the purpose of the Nvidia Spectrum-X networking platform?**

A. To provide standard networking capabilities  
B. To optimize networking performance specifically for AI and data-intensive workloads  
C. To eliminate the need for networks altogether  
D. To serve as a simple switch  

**Answer:** B. To optimize networking performance specifically for AI and data-intensive workloads  

---

**37. How does Spectrum-X improve the performance of Ethernet-based AI clouds?**

A. By increasing latency  
B. By offering high throughput, low latency, and enhanced congestion management tailored for AI applications  
C. By reducing the number of switches needed  
D. By focusing on wireless technology  

**Answer:** B. By offering high throughput, low latency, and enhanced congestion management tailored for AI applications  

---

**38. What advantages does the combination of Spectrum-4 switches and BlueField-3 DPUs offer?**

A. Slower data transfer  
B. Enhanced performance, scalability, and security for AI workloads  
C. Increased complexity without benefits  
D. Reduced network capacity  

**Answer:** B. Enhanced performance, scalability, and security for AI workloads  

---

**39. How does Spectrum-X achieve effective bandwidth for AI workloads?**

A. By limiting the number of devices on the network  
B. Through advanced traffic management and efficient resource allocation  
C. By reducing the speed of data transfer  
D. By using only traditional Ethernet technology  

**Answer:** B. Through advanced traffic management and efficient resource allocation  

---

**40. What unique features make Spectrum-X suitable for AI, machine learning, and natural language processing?**

A. Its simplicity and low performance  
B. High bandwidth, low latency, and advanced routing capabilities designed for data-intensive applications  
C. Limited capabilities compared to older models  
D. Focus only on traditional networking solutions  

**Answer:** B. High bandwidth, low latency, and advanced routing capabilities designed for data-intensive applications  

---

### Advanced Features and Enhancements

**41. How does Nvidia's RoCE adaptive routing technology enhance network performance?**

A. By slowing down data transfer  
B. By dynamically adjusting paths to minimize congestion and improve data flow efficiency  
C. By increasing the number of required network devices  
D. By simplifying the network architecture  

**Answer:** B. By dynamically adjusting paths to minimize congestion and improve data flow efficiency  

---

**42. What is the function of Nvidia's RoCE congestion control mechanism?**

A. To increase network congestion  
B. To manage and alleviate congestion, ensuring stable and efficient data transfer across the network  
C. To limit the number of data packets sent  
D. To eliminate the need for network management  

**Answer:** B. To manage and alleviate congestion, ensuring stable and efficient data transfer across the network  

---

**43. How does RoCE congestion control improve burst tolerance in Ethernet networks?**

A. By allowing more data packets to be lost  
B. By smoothing out data flow during high traffic periods, preventing packet loss and latency spikes  
C. By reducing the speed of data transfer  
D. By using only traditional protocols  

**Answer:** B. By smoothing out data flow during high traffic periods, preventing packet loss and latency spikes  

---

**44. What requirements must be met for RoCE adaptive routing and congestion control to function effectively?**

A. Complex hardware setups  
B. Compatible hardware, proper configuration, and effective management protocols  
C. Limited network infrastructure  
D. No special requirements  

**Answer:** B. Compatible hardware, proper configuration, and effective management protocols  

---

**45. How do these technologies contribute to overall network utilization in AI data centers?**

A. They reduce the need for bandwidth  
B. By optimizing data flows and minimizing congestion, leading to better resource utilization and performance  
C. They complicate the network architecture  
D. They have no significant impact  

**Answer:** B. By optimizing data flows and minimizing congestion, leading to better resource utilization and performance  

Here are multiple-choice questions based on your course material, along with the correct answers:

---

### Future Considerations

**46. How might advancements in Ethernet and InfiniBand technologies influence AI data centers?**

A. By limiting bandwidth  
B. By enabling higher speeds and lower latency, improving overall AI performance and scalability  
C. By complicating network management  
D. By making data centers less efficient  

**Answer:** B. By enabling higher speeds and lower latency, improving overall AI performance and scalability  

---

**47. What trends are emerging in the networking landscape for AI workloads?**

A. Decreased reliance on networked systems  
B. Increased use of AI-optimized networking protocols and technologies to support demanding workloads  
C. A move back to traditional networking methods  
D. Reduced bandwidth requirements  

**Answer:** B. Increased use of AI-optimized networking protocols and technologies to support demanding workloads  

---

**48. How can organizations leverage networking technologies to improve AI performance?**

A. By using outdated networking equipment  
B. By adopting high-performance networking solutions like RDMA and InfiniBand for reduced latency and increased throughput  
C. By simplifying network architecture without improving speed  
D. By minimizing the use of network resources  

**Answer:** B. By adopting high-performance networking solutions like RDMA and InfiniBand for reduced latency and increased throughput  

---

**49. What future developments can we expect in NVIDIA's networking portfolio?**

A. A shift towards slower networking technologies  
B. Continued innovation in high-speed networking solutions and enhanced integration with AI workloads  
C. No significant changes expected  
D. Focus only on traditional networking  

**Answer:** B. Continued innovation in high-speed networking solutions and enhanced integration with AI workloads  

---

**50. How will the evolution of networking standards impact AI data center operations?**

A. It will complicate operations and reduce efficiency  
B. Improved standards will enhance interoperability, scalability, and performance of AI data centers  
C. There will be no impact on operations  
D. Networking standards will become obsolete  

**Answer:** B. Improved standards will enhance interoperability, scalability, and performance of AI data centers  

---

### Technical Challenges

**51. What are the potential challenges of integrating InfiniBand and Ethernet in a hybrid networking environment?**

A. There are no challenges; they work perfectly together  
B. Compatibility issues, management complexity, and performance tuning can pose significant challenges  
C. Only InfiniBand can be integrated with Ethernet  
D. Ethernet will always outperform InfiniBand  

**Answer:** B. Compatibility issues, management complexity, and performance tuning can pose significant challenges  

---

**52. How can network congestion affect AI workloads, and what strategies can mitigate it?**

A. It has no impact on performance  
B. Congestion can lead to increased latency and reduced throughput; strategies include traffic management and resource allocation  
C. Congestion only affects storage, not networking  
D. It will improve performance by forcing faster data transfers  

**Answer:** B. Congestion can lead to increased latency and reduced throughput; strategies include traffic management and resource allocation  

---

**53. What considerations should be made when designing a network for AI workloads?**

A. Only cost should be considered  
B. Factors such as bandwidth, latency, scalability, and network topology are critical for optimal AI performance  
C. Security is not a priority  
D. Simplicity is more important than performance  

**Answer:** B. Factors such as bandwidth, latency, scalability, and network topology are critical for optimal AI performance  

---

**54. How can organizations ensure the reliability and security of their data center networks?**

A. By ignoring updates and patches  
B. Implementing robust security measures, regular monitoring, and network redundancy  
C. Relying solely on hardware  
D. Limiting network access for all users  

**Answer:** B. Implementing robust security measures, regular monitoring, and network redundancy  

---

**55. What role does network management play in optimizing AI data center performance?**

A. It complicates operations  
B. Effective network management ensures optimal resource utilization, minimizes latency, and maximizes throughput  
C. It is unnecessary in modern data centers  
D. Network management has no impact on performance  

**Answer:** B. Effective network management ensures optimal resource utilization, minimizes latency, and maximizes throughput  

---

### Historical Context

**56. How has the role of networking in data centers evolved over the years?**

A. Networking has become less important  
B. It has shifted from simple connectivity to complex, high-speed, and efficient data transfer technologies tailored for demanding workloads  
C. Networking now only serves basic functions  
D. The focus has only been on storage solutions  

**Answer:** B. It has shifted from simple connectivity to complex, high-speed, and efficient data transfer technologies tailored for demanding workloads  

---

**57. What significant milestones have marked the development of InfiniBand and Ethernet technologies?**

A. There have been no significant developments  
B. Key milestones include the introduction of RDMA for low-latency communication and the evolution of Ethernet speeds from 10Mbps to 400Gbps and beyond  
C. Only Ethernet has seen significant changes  
D. InfiniBand has become obsolete  

**Answer:** B. Key milestones include the introduction of RDMA for low-latency communication and the evolution of Ethernet speeds from 10Mbps to 400Gbps and beyond  

---

**58. How do the historical developments in networking standards inform current practices in AI data centers?**

A. They have no relevance to current practices  
B. Historical developments guide the selection of technologies, protocols, and architectures that best meet the demands of modern AI applications  
C. Only past Ethernet standards matter  
D. Old standards are always superior  

**Answer:** B. Historical developments guide the selection of technologies, protocols, and architectures that best meet the demands of modern AI applications  

---

**59. What impact have NVIDIA's innovations had on the networking industry for AI?**

A. They have made networking less important  
B. NVIDIA's innovations have driven advancements in high-performance networking technologies that support AI workloads and improved efficiency in data centers  
C. Innovations have created more confusion  
D. Only storage innovations are significant  

**Answer:** B. NVIDIA's innovations have driven advancements in high-performance networking technologies that support AI workloads and improved efficiency in data centers  

---

**60. How does the evolution of network protocols affect the scalability of AI applications?**

A. New protocols do not influence scalability  
B. Evolving protocols enable better bandwidth management, lower latency, and greater efficiency, which are essential for scaling AI applications  
C. They only complicate scalability  
D. Scalability is independent of networking  

**Answer:** B. Evolving protocols enable better bandwidth management, lower latency, and greater efficiency, which are essential for scaling AI applications  

---

### Performance Evaluation

**61. How can organizations measure the effectiveness of their AI data center networking solutions?**

A. By ignoring network metrics  
B. By using performance metrics such as throughput, latency, and packet loss to evaluate network performance  
C. Only by comparing costs  
D. There are no effective measures  

**Answer:** B. By using performance metrics such as throughput, latency, and packet loss to evaluate network performance  

---

**62. What benchmarks are commonly used to assess networking performance in AI workloads?**

A. Only storage benchmarks  
B. Benchmarks such as bandwidth tests, latency measurements, and application-specific performance metrics  
C. No benchmarks are necessary  
D. Only synthetic benchmarks  

**Answer:** B. Benchmarks such as bandwidth tests, latency measurements, and application-specific performance metrics  

---

**63. How do network configurations influence the training time of AI models?**

A. They have no effect on training time  
B. Proper network configurations can reduce training time by optimizing data transfer rates and minimizing latency  
C. Only hardware influences training time  
D. Network configurations can only slow down training  

**Answer:** B. Proper network configurations can reduce training time by optimizing data transfer rates and minimizing latency  

---

**64. What metrics should be monitored to ensure optimal network performance in AI data centers?**

A. Only network speed  
B. Metrics such as bandwidth utilization, latency, packet loss, and error rates should be monitored  
C. No specific metrics are needed  
D. Only storage metrics are relevant  

**Answer:** B. Metrics such as bandwidth utilization, latency, packet loss, and error rates should be monitored  

---

**65. How can organizations validate the performance of their networking hardware and software?**

A. By relying on vendor claims only  
B. Through rigorous testing and benchmarking against industry standards to ensure they meet performance expectations  
C. Performance validation is unnecessary  
D. Only by comparing with older systems  

**Answer:** B. Through rigorous testing and benchmarking against industry standards to ensure they meet performance expectations  

---

### Integration and Deployment

**66. What best practices should organizations follow when deploying networking solutions in AI data centers?**

A. Ignore scalability considerations  
B. Implement redundancy, optimize for low latency, and ensure proper monitoring and management tools are in place  
C. Focus only on cost reduction  
D. Use outdated technologies  

**Answer:** B. Implement redundancy, optimize for low latency, and ensure proper monitoring and management tools are in place  

---

**67. How can businesses ensure their network architecture supports both small-scale and large-scale AI workloads?**

A. By using the same equipment for all workloads  
B. Designing a flexible and scalable architecture that can adapt to varying demands and workload sizes  
C. Focusing solely on small-scale deployments  
D. Avoiding upgrades until necessary  

**Answer:** B. Designing a flexible and scalable architecture that can adapt to varying demands and workload sizes  

---

**68. What training or resources are available for teams implementing NVIDIA networking technologies?**

A. No training resources are available  
B. NVIDIA provides comprehensive documentation, training programs, and certification courses for networking technologies  
C. Only external training providers can offer relevant courses  
D. Teams should learn from trial and error  

**Answer:** B. NVIDIA provides comprehensive documentation, training programs, and certification courses for networking technologies  

---

**69. How do organizations manage interoperability challenges in a multi-vendor networking environment?**

A. By standardizing on a single vendor's products only  
B. Implementing open standards and protocols to ensure compatibility and conducting thorough testing across different vendor solutions  
C. Avoiding multi-vendor environments altogether  
D. Relying solely on vendor support for integration issues  

**Answer:** B. Implementing open standards and protocols to ensure compatibility and conducting thorough testing across different vendor solutions  

---

**70. What role does ongoing maintenance play in the performance of AI data center networks?**

A. Ongoing maintenance is not important  
B. Regular maintenance ensures network reliability, performance optimization, and the timely application of updates and security patches  
C. Maintenance only affects hardware, not networks  
D. Only initial deployment is critical; ongoing maintenance is optional  

**Answer:** B. Regular maintenance ensures network reliability, performance optimization, and the timely application of updates and security patches