# Functional Requirements

## Requirements for Value-Seeking Budgeter (hybrid_P1)

### Derived from Group: hybrid_G1

# Requirement ID: FR_hybrid_1

- Description: The system shall allow users to view and export their historical mood data regardless of subscription status.
- Source Persona: Value-Seeking Budgeter
- Traceability: hybrid_G1
- Acceptance Criteria:
  - Given a user with an expired subscription,
  - When they navigate to the "History" or "Data Export" section,
  - Then they shall be able to see their previous entries without being blocked by a paywall.
- Notes: Rewritten to address the specific pain point identified in hybrid_G1 where users feel previous data is hidden behind a paywall.

# Requirement ID: FR_hybrid_2

- Description: The system shall display the full monthly and annual cost of premium plans on the initial subscription splash screen.
- Source Persona: Value-Seeking Budgeter
- Traceability: hybrid_G1
- Acceptance Criteria:
  - Given the user is viewing the "Go Premium" screen,
  - When they review the available plans,
  - Then the exact price per billing cycle must be visible without requiring the user to click into secondary links.
- Notes: Improves transparency to prevent "unexpected charges" concerns noted in the group feedback. Made it more verifiable and decisive instead of using 'or'.

## Requirements for Global Experience Evaluator (hybrid_P2)

### Derived from Group: hybrid_G2

# Requirement ID: FR_hybrid_3

- Description: The system shall provide a language selection menu within the "Settings" tab that allows the user to change the app interface to supported languages.
- Source Persona: Global Experience Evaluator
- Traceability: auto_G2
- Acceptance Criteria:
  - Given the user is in the "Settings" menu,
  - When they select a new language from the dropdown,
  - Then all UI text elements shall update to the selected language immediately.
- Notes: Auto requirement was far too vague, chose specific function directly addressing the hybrid_G2 feedback stating the user "cannot change the language".

# Requirement ID: FR_hybrid_4

- Description: The system shall support a "Quick Log" widget for mobile home screens to allow mood entry in under three interactions.
- Source Persona: Global Experience Evaluator
- Traceability: auto_G2
- Acceptance Criteria:
  - Given the user has the app widget on their home screen,
  - When they tap a mood icon on the widget,
  - Then the entry shall be saved to the database without requiring navigation through the main dashboard.
- Notes: Targets a specific constraint of limited time for data entry during daily check-ins instead of vague high-level goal.

## Requirements for Insight-Driven Self-Tracker (hybrid_P3)

### Derived from Group: hybrid_G3

# Requirement ID: FR_hybrid_5

- Description: The system shall include "Stressed" and "Overwhelmed" as selectable primary emotional states in the daily check-in flow.
- Source Persona: Insight-Driven Self-Tracker
- Traceability: hybrid_G3
- Acceptance Criteria:
  - Given the user is performing a daily check-in,
  - When they reach the emotion selection screen,
  - Then "Stressed" must be one of the displayed options.
- Notes: Corrects the limited emotional vocabulary identified in user reviews where users found emotion choices limited.

# Requirement ID: FR_hybrid_6

- Description: The system shall generate a monthly "Mental Health Trend Report" that correlates mood scores with completed content or courses.
- Source Persona: Insight-Driven Self-Tracker
- Traceability: hybrid_G3
- Acceptance Criteria:
  - Given the user has logged data for a month,
  - When the monthly report is generated,
  - Then it must include a visual representation of progress alongside markers for completed educational courses.
- Notes: Addresses the goal of gaining deeper insights and monitoring well-being over time.

## Requirements for Stability-First Daily User (hybrid_P4)

### Derived from Group: hybrid_G4

# Requirement ID: FR_hybrid_7

- Description: The system shall limit "Review the App" pop-up prompts to a maximum of once every 90 days per user.
- Source Persona: Stability-First Daily User
- Traceability: auto_G4
- Acceptance Criteria:
  - Given a user who has seen a review prompt in the last 90 days,
  - When they launch the app,
  - Then no review request pop-up shall be displayed.
- Notes: Directly addresses the pain point of repetitive and intrusive review requests.

# Requirement ID: FR_hybrid_8

- Description: The system shall implement an offline-first mechanism that saves mood logs locally if an internet connection is lost.
- Source Persona: Stability-First Daily User
- Traceability: auto_G4
- Acceptance Criteria:
  - Given the user is offline,
  - When they submit a log entry,
  - Then the app shall confirm it is saved locally and sync once a connection is restored.
- Notes: Prevents data loss during technical failures mentioned in the G4 review group.

## Requirements for Clinical Transitioner (hybrid_P5)

### Derived from Group: hybrid_G5

# Requirement ID: FR_hybrid_9

- Description: The system shall provide a feature to generate a password-protected PDF therapy report of the user's mood history.
- Source Persona: Clinical Transitioner
- Traceability: auto_G5
- Acceptance Criteria:
  - Given the user selects "Generate Therapy Report,"
  - When the file is created,
  - Then the user must be prompted to set a 4-digit PIN for the document before it can be exported.
- Notes: Supports the persona's goal of sharing realistic data with clinical professionals.

# Requirement ID: FR_hybrid_10

- Description: The system shall provide a search interface that filters a database of licensed healthcare professionals by three mandatory criteria: medical specialty, geographic radius (in kilometers), and real-time appointment availability.
- Source Persona: Clinical Transitioner
- Traceability: auto_G5
- Acceptance Criteria:
  - Given the user is on the "Find a Professional" screen,
  - When the user applies a filter for a specific specialty (e.g., "Psychologist") and a location radius (e.g., "within 10km"),
  - Then the system shall display a list of matching profiles in less than 2.0 seconds, where each profile card contains a "Credentials Verified" badge, a clickable phone number, and a "Book Now" button for available time slots.
- Notes: Rewritten to make specific and measureable.
