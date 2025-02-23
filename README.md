# Assitive-Ambient-Intelligence
# Overview
The proposed system is an RFID-enabled wearable device designed to assist dementia patients in tracking and completing their daily tasks. The system ensures remote monitoring by caregivers, reducing their workload while maintaining patient autonomy. The wearable device scans RFID tags placed in different locations within a patient's environment, automatically logging task completion.
# Components Used
1.**RFID Scanner:** Detects RFID tags placed at task locations.

2.**RFID Tags:** Passive tags placed at different locations like medicine cabinets and dining areas.

3.**Microcontroller Unit (MCU):** Processes data from the RFID scanner and manages communication.

4.**Web-based Dashboard:** Displays task logs for caregivers in real time.

# Flowchart
![Flowchart](https://github.com/user-attachments/assets/6c903e36-9647-4dce-b99d-b1bab9624494)
# Block Diagram
![Block Diagram](https://github.com/user-attachments/assets/0fa2eb1c-818f-419c-9870-fb8a47286000)
# Working
.The caregiver pre-sets daily tasks using the web application.

.When a patient completes a task, the RFID scanner detects the tag.

.The microcontroller processes the data and updates the caregiver’s dashboard.

.If the patient misses a task, the Patient Activity Tracker displays the information in red color; otherwise, completed tasks are displayed in green color, which can be monitored by the patient's caregiver.

# Environment Used
**Raspberry Pi 4B:** Serves as the primary computational unit.

**RC522 RFID Scanner:** Detects RFID tags for task tracking.

**RFID Tags:** Placed at strategic locations to track task completion.

**Flask Framework:** Used for developing the web-based dashboard.

# Future Scope
.GPS Integration:To track patient movement and prevent wandering.

.Integration with AI: Predictive analytics to detect behavior changes and send proactive alerts.

.Smartphone App: For caregivers to track real-time task completion on mobile devices.

# Conclusion
The RFID-enabled wearable device offers a non-intrusive and efficient solution for monitoring dementia patients’ daily activities. By automating task tracking, caregivers can reduce stress and ensure timely interventions. The system enhances patient autonomy while improving the quality of caregiving
