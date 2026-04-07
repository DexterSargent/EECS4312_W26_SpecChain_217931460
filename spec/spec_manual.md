# Requirement ID: FR1

- Description: [The system shall provide read-only access to reports generated during the trial period for 12 months after trial period ends.]
- Source Persona: [Cost-conscious explorer]
- Traceability: [Derived from review group G1]
- Acceptance Criteria: [Given the user has no active subscription and registered within 12 months, when the user views the reports page, all reports are accessible as pdf files.]

# Requirement ID: FR2

- Description: [The system shall maintain a local cache of all mood entries and associated user notes for a rolling period of 72 hours from the timestamp of creation]
- Source Persona: [Frustrated reliability-seeker]
- Traceability: [Derived from review group G2]
- Acceptance Criteria: [Given the device has no internet access, when the user views their log history, Then all entries created within the last 72 hours must be visible and editable.]

# Requirement ID: FR3

- Description: [The system shall deliver a push notification for a scheduled mood check-in within 60 seconds of the user-defined time.]
- Source Persona: [Frustrated reliability-seeker]
- Traceability: [Derived from review group G2]
- Acceptance Criteria: Given a scheduled check-in at 09:00, when the system clock reaches 09:00, Then a notification is received on the device before 09:01.

# Requirement ID: FR4

- Description: [The system shall support dynamic text scaling that allows users to increase font sizes up to 200% without text truncation or UI overlapping].
- Source Persona: [Accessibility focused user]
- Traceability: [Derived from review group G3]
- Acceptance Criteria: [Given the system-wide font size is set to "200%" when the app is opened, all labels and body text must remain fully visible and readable within their containers.]

# Requirement ID: FR5

- Description: [The system shall display a "Crisis Support" button on all screens that initiates a pop-up with call, text, and email options to national crisis supports.]
- Source Persona: [Accessibility focused user]
- Traceability: [Derived from review group G3]
- Acceptance Criteria: [When the user taps the "Crisis Support" button and selects an option (call/text/email), then the device native messaging app opens.]

# Requirement ID: FR6

- Description: [The system shall provide a high-contrast display mode that meets WCAG 2.2 AAA contrast ratio standards.]
- Source Persona: [Accessibility focused user]
- Traceability: [Derived from review group G3]
- Acceptance Criteria: [Contrast ratio greater than 7:1 for all text elements, mode can be toggled on and off, all screens/pages reflect selected mode]

# Requirement ID: FR7

- Description: [The system shall provide a keyword search function that returns all matching notes in less than 500 milliseconds].
- Source Persona: [Insight-driven tracker]
- Traceability: [Derived from review group G4]
- Acceptance Criteria: [When the user enters a search term, the results list must filter and display matching entries in under 500 milliseconds.]

# Requirement ID: FR8

- Description: [The system shall provide trend visualizations once the user has logged at least 5 mood entries]
- Source Persona: [Insight-driven tracker]
- Traceability: [Derived from review group G4]
- Acceptance Criteria: [Given a user has successfully saved 5 or more unique mood entries, when the user accesses the "Insights" dashboard, Then the system shall render a mood trend line graph representing those entries within 1.5 seconds.]

# Requirement ID: FR9

- Description: [The system shall generate a PDF document containing a chronological list of all mood entries and user notes for the preceding 30-day period.]
- Source Persona: [Clinical patient-collaborator]
- Traceability: [Derived from review group G5]
- Acceptance Criteria: [When the user selects "Generate 30-Day Report," Then the system produces a PDF file containing every log entry from the last 30 days.]

# Requirement ID: FR10

- Description: [The system shall provide an encrypted transfer function for sharing generated PDF reports with a user-specified email recipient.]
- Source Persona: [Clinical patient-collaborator]
- Traceability: [Derived from review group G5]
- Acceptance Criteria: [When the user confirms a report sharing action, then the system sends a secure link to the recipient email that expires within 24 hours.]
