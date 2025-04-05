# Project Title: Financial Estate Management

## 1. Project Overview & Goal

*   **Purpose:**
    To create a simple, modern, and sleek **web-based application**, accessible via desktop and tablet browsers, for entering and managing financial client personal information and their associated insurance policies.

*   **Target User:**
    *   **Primary:** Financial Service Managers (like myself) needing an efficient, modern tool for personal client and policy data entry, management, and portfolio visualization (both overall business and individual client views).
    *   **Secondary Consideration:** The design should be clean and functional, potentially serving as a foundation that could later be adapted for use by individual Financial Service Representatives.

*   **Key Objectives:**
    *   Provide a web-based UI for seamless cross-platform data entry and access (Windows, macOS, iPadOS).
    *   Ensure full data ownership, privacy, and control through self-hosting on local storage/personal NAS.
    *   Implement business intelligence features to visualize and analyze the overall business portfolio (e.g., by Policy Type, Client Gender).
    *   Enable clear presentation of individual client portfolios through visualizations, organized by Policy Type and Coverage Type, to support client reviews.


## 2. Core Features / Functionality

This section lists the primary capabilities the application must provide to the user.

*   **Dashboard / Overview:**
    *   [ ] Display a main dashboard or overview screen upon login/launch (potentially showing quick stats or links to key sections).

*   **Client Management:**
    *   [ ] **Add:** Create new client records via a dedicated form.
    *   [ ] **List & View:** Display a list of all clients (e.g., using summary cards). This list should be:
        *   **Searchable:** Primarily by client `FullName` and `Personal_ID` via the main header search bar.
        *   **Sortable:** Allow sorting the client list (e.g., by `FullName`, `DateAdded`).
    *   [ ] **Select & View Details:** Select a client from the list to view their full details (personal information and associated policies) in a dedicated view.
    *   [ ] **Update:** Edit and save changes to existing client information.
    *   [ ] **Delete:** Remove a client record. *(Note: Consider implications - deleting a client might require deleting associated policies or handling orphaned records. Soft delete/archiving might be safer long-term but adds complexity).*

*   **Policy Management (within a selected Client's context):**
    *   [ ] **Add:** Create new insurance policy records, ensuring each new policy is correctly linked to the currently viewed client.
    *   [ ] **List & View:** Display all policies associated with the selected client (e.g., using policy cards). This list should be:
        *   **Sortable:** Allow sorting the policies (e.g., by `PolicyType`, `InceptionDate`, `PolicyNumber`).
    *   [ ] **Select & View Details:** Select a policy... displaying its details and associated coverages in the two-card layout.
    *   [ ] **Update:** Edit and save changes to existing policy information *and its associated coverages*.
    *   [ ] **Delete:** Remove a policy record *and all its associated coverage records*.
    *   [ ] **Manage Policy Coverages:** Within the policy edit view, allow users to add, view, update, and delete individual coverage lines using the dynamic row interface ("+" / "-" buttons).
    *   [ ] **Calculate & Display:** Automatically calculate and display the `Annualised_Premium` based on `PremiumAmount` and `PremiumFrequency` in the Policy Details card.

*   **Search & Data Retrieval:**
    *   [ ] Implement the global **Search Bar** in the header for quick client lookup (`FullName`, `Personal_ID`) and potentially policy lookup (`PolicyNumber`).

*   **Reporting & Visualization:**
    *   [ ] **Business Portfolio Visualization:** Provide a dedicated view or dashboard section to visualize the overall business portfolio. This must include:
        *   Data aggregation based on all clients/policies.
        *   Visual representations (e.g., charts - Pie and Bar charts preferred) of the portfolio breakdown.
        *   Ability to **filter/group** the visualization by `PolicyType` and client `Gender`.
    *   [ ] **Client Portfolio Visualization:** Within the individual client detail view, provide a visualization of that specific client's insurance portfolio. This must include:
        *   Visual representations (e.g., charts) showing the client's policy distribution.
        *   Ability to **filter/group/sort** the visualization by `PolicyType` and `CoverageType`.

*   **Data Handling & Persistence:**
    *   [ ] **Persistence:** Reliably save all client, policy, and coverage data to the designated database (SQLite file initially).
    *   [ ] **Validation:** Implement input validation based on the defined database schema (e.g., ensure required fields are filled, data types match like valid dates/email formats, numeric fields contain numbers). Provide user-friendly error messages for validation failures.


## 3. User Interface (UI) / User Experience (UX) Requirements

*   **Overall Aesthetic:**
    *   Target a **clean, modern, and sleek** visual style.
    *   Prioritize an interface that is **easy on the eyes**, suitable for potentially long data entry sessions (good contrast, legible typography, ample whitespace).
    *   Maintain a professional look and feel appropriate for financial services.
    *   Consider a palette based on Neutral & Accent:
        *   Base: White, light gray, or beige
        *   Primary: A rich, saturated color like a deep blue, teal, or a muted green
        *   Secondary: A contrasting accent color, such as a vibrant yellow, orange, or pink

*   **Layout & Navigation Structure:**
    *   **Primary Navigation:** Implement a **vertical sidebar** on the left side for main application sections (e.g., 'Dashboard/Overview', 'Clients', 'Reports', 'Settings'). This provides a clear hierarchy and is space-efficient for content areas.
    *   **Header:** Utilize a **sticky/fixed header** at the top of the page. This ensures consistent access to key functions regardless of scroll position.
    *   **Search:** Include a **prominent search bar** within the sticky header for efficient data retrieval as defined in Core Features.
    *   **Content Area:** The main area to the right of the sidebar and below the header will display the core content (client lists, forms, dashboards).
    *   **Breadcrumbs:** Implement breadcrumbs, likely displayed below the header or at the top of the content area, to show the user's current location within the application's hierarchy (e.g., `Home > Clients > [Client Name] > Edit Policy`).

*   **Content Display & Interaction:**
    *   **Card-Based Layout:** Use a **card-based layout** within the main content area to segment and display lists of items clearly (e.g., Client list uses summary cards, a Client's Policies view shows policy cards). Consider a grid layout for these cards where appropriate.
    *   **Forms:** Data entry forms should be well-structured within the content area, using clear labels, logical grouping of fields, and appropriate input controls (text fields, date pickers, dropdowns, etc.).
        *   **Specific Controls:**
            *   The `Gender` field **must** be presented using **radio buttons** offering exactly two choices: 'Male' and 'Female'. Only one option can be selected.
            *   Fields like `Salutation`, `SmokingStatus`, `MaritalStatus` should also use radio buttons with their respective predefined options.
            *   Use appropriate dropdowns (`<select>`) for `Res_Country`, `Mail_Country`, `PolicyType`, `InsuranceProvider`, `PremiumFrequency`, `PaymentMode`, `BenefitLevel`, `CoverageType`.
            *   Use date picker components for date fields (`DateOfBirth`, `InceptionDate`, etc.) that display in `DD/MM/YYYY` format but handle data as `YYYY-MM-DD`.
            *   Implement the "Mailing Address same as Residential" checkbox logic as previously described (hiding/showing/copying fields).
    *   **Transitions & Feedback:** Implement **smooth transitions and subtle animations** where appropriate (e.g., loading states, expanding details). Provide clear visual feedback for user actions (button clicks, saves, errors).
    *   **Policy View Layout:** When viewing/editing a specific policy, the information should be presented in two distinct cards:
        *   **Card 1: "Policy Details":** Contains the form fields corresponding to the `Policies` table (`PolicyNumber`, `PlanName`, `PolicyType`, `InsuranceProvider`, dates, premium details, etc.). Display the calculated `Annualised_Premium` as a read-only field near the `PremiumAmount` and `PremiumFrequency` fields.
        *   **Card 2: "Policy Coverages":** Contains the details for the individual coverages/riders associated with the policy.
            *   This card should be **visually wider** than the Policy Details card, if possible, to accommodate fields horizontally.
            *   Display coverages in a **table-like structure** or repeating rows. Each row corresponds to one record from the `Coverages` table linked to the current policy.
            *   Each row should contain input fields for `CoveragePlanName`, `BenefitLevel` (dropdown), `CoverageType` (dropdown), `CoveragePremiumAmount`, `CoverageSumAssured`, dates, `CoverageTillAge`.
            *   **Dynamic Row Management:**
                *   Include a clearly visible **"+" (Add Row) button/icon**, likely placed below the last coverage row or in the card's header/footer. Clicking this adds a new, blank row of coverage input fields to the UI.
                *   Include a clearly visible **"-" (Remove Row) button/icon** next to *each* existing coverage row. Clicking this removes that specific row from the UI and its corresponding data upon saving.
            *   The layout within each coverage row should attempt to keep fields on a **single line** for space efficiency, wrapping if necessary on smaller screens.

*   **Key Design Principles:**
    *   **Consistency:** Maintain a consistent design language (colors, typography, component styles, interaction patterns) throughout the application.
    *   **Accessibility:** Ensure the UI is accessible. Use clear labels, sufficient color contrast, appropriate spacing, and keyboard navigability where feasible. Follow standard accessibility guidelines (WCAG).

*   **Responsiveness & Cross-Platform:**
    *   **Mobile Optimization:** The web UI *must* be responsive and adapt gracefully to different screen sizes, including tablets (iPadOS) and potentially smaller mobile viewports. For smaller screens, the vertical sidebar might collapse into a hamburger menu, and horizontal layouts (like coverage rows) may need to stack vertically.

## 4. Data Structure / Database Schema

*   **Client Information Table (`Clients`):**
    *   `ClientID` (INTEGER) - *Primary Key, Auto-incrementing*
    *   `Personal_ID` (TEXT) - *Required, Store as entered, display logic for uppercase handled by UI*
    *   `Salutation` (TEXT) - *Required. Input via radio buttons: 'Mr', 'Ms', 'Mrs', 'Dr'. Value stored will be one of these.*
    *   `FullName` (TEXT) - *Required, Store as entered, display logic for proper case handled by UI*
    *   `DateOfBirth` (TEXT) - *Required, Store in ISO format (YYYY-MM-DD) recommended for sorting/querying, display format DD/MM/YYYY handled by UI*
    *   `Gender` (TEXT) - *Required. Input via radio buttons: 'Male', 'Female'. Value stored will be 'Male' or 'Female'.*
    *   `SmokingStatus` (TEXT) - *Required. Input via radio buttons: 'Smoker', 'Non-Smoker'. Value stored will be one of these.*
    *   `MaritalStatus` (TEXT) - *Required. Input via radio buttons: 'Single', 'Married', 'Divorced', 'Widowed'. Value stored will be one of these.*
    *   `Occupation` (TEXT) - *Nullable. Store as entered, display logic for proper case handled by UI*
    *   `Annual_Income` (INTEGER) - *Nullable. Store as number (integer), display formatting with commas handled by UI*
    *   `Mobile_Phone` (TEXT) - *Required*
    *   `Personal_Email` (TEXT) - *Required, Validate format*
    *   **--- Residential Address Fields ---**
    *   `Res_Block_House_No` (TEXT) - *Nullable. Store as entered, display logic for uppercase handled by UI*
    *   `Res_Street_Name` (TEXT) - *Nullable. Store as entered, display logic for proper case handled by UI*
    *   `Res_Unit_No` (TEXT) - *Nullable*
    *   `Res_Postal_Code` (TEXT) - *Required*
    *   `Res_Country` (TEXT) - *Required, Default 'Singapore'. Value from predefined list.*
    *   **--- Mailing Address Fields ---**
    *   `IsMailingSameAsResidential` (INTEGER) - *Required, Default 1 (TRUE). 0 for FALSE.*
    *   `Mail_Block_House_No` (TEXT) - *Nullable, Store as entered, display logic for uppercase handled by UI*
    *   `Mail_Street_Name` (TEXT) - *Nullable, Store as entered, display logic for proper case handled by UI*
    *   `Mail_Unit_No` (TEXT) - *Nullable*
    *   `Mail_Postal_Code` (TEXT) - *Nullable*
    *   `Mail_Country` (TEXT) - *Nullable. Value from predefined list.*
    *   **--- Metadata ---**
    *   `DateAdded` (TEXT) - *Auto-generated (Default to current timestamp 'YYYY-MM-DD HH:MM:SS' on insert)*
    *   `LastUpdated` (TEXT) - *Auto-updated (Update to current timestamp 'YYYY-MM-DD HH:MM:SS' on update)*

*   **Policy Information Table (`Policies`):**
    *   `PolicyID` (INTEGER) - *Primary Key, Auto-incrementing*
    *   `ClientID` (INTEGER) - *Required, Foreign Key linking to Clients(ClientID)*
    *   `PolicyNumber` (TEXT) - *Required, Often alphanumeric*
    *   `PlanName` (TEXT) - *Required (The overall name of the policy product)*
    *   `PolicyType` (TEXT) - *Required. Value from predefined list.*
    *   `InsuranceProvider` (TEXT) - *Required. Value from predefined list.*
    *   `InceptionDate` (TEXT) - *Required. Store as YYYY-MM-DD.*
    *   `MaturityExpiryDate` (TEXT) - *Nullable. Store as YYYY-MM-DD.*
    *   `PremiumAmount` (REAL) - *Required. Base premium per frequency. Use REAL for potential decimal values.*
    *   `PremiumFrequency` (TEXT) - *Required. Value from predefined list.*
    *   `PremiumTermYears` (INTEGER) - *Required. Duration of premium payment in years.*
    *   `PaymentMode` (TEXT) - *Required. Value from predefined list.*
    *   `DateAdded` (TEXT) - *Auto-generated (Default to current timestamp 'YYYY-MM-DD HH:MM:SS' on insert)*
    *   `LastUpdated` (TEXT) - *Auto-updated (Update to current timestamp 'YYYY-MM-DD HH:MM:SS' on update)*

*   **Policy Coverage Table (`Coverages`):** *(Represents individual benefits/riders within a Policy)*
    *   `CoverageID` (INTEGER) - *Primary Key, Auto-incrementing*
    *   `PolicyID` (INTEGER) - *Required, Foreign Key linking to Policies(PolicyID)*
    *   `CoveragePlanName` (TEXT) - *Required. Specific name of the coverage/rider.*
    *   `BenefitLevel` (TEXT) - *Required. Value from predefined list ('Main Plan', 'Rider').*
    *   `CoverageType` (TEXT) - *Required. Value from predefined list.*
    *   `CoveragePremiumAmount` (REAL) - *Nullable. Premium specifically for this coverage/rider.*
    *   `CoverageSumAssured` (REAL) - *Required. The benefit amount for this specific coverage.*
    *   `CoverageInceptionDate` (TEXT) - *Required. Store as YYYY-MM-DD.*
    *   `CoverageMaturityExpiryDate` (TEXT) - *Nullable. Store as YYYY-MM-DD.*
    *   `CoverageTillAge` (INTEGER) - *Nullable. Age until which this specific coverage lasts.*
    *   `DateAdded` (TEXT) - *Auto-generated (Default to current timestamp 'YYYY-MM-DD HH:MM:SS' on insert)*
    *   `LastUpdated` (TEXT) - *Auto-updated (Update to current timestamp 'YYYY-MM-DD HH:MM:SS' on update)*

*   **Relationship:** One `Clients` record relates to potentially many `Policies` records. One `Policies` record can have multiple related `Coverages` records.

*   **Dropdown Lists & Defaults:**
    *   `Country` (Clients - Res & Mail):
        *   Default: Singapore
        *   Southeast Asia: Brunei, Cambodia, Indonesia, Malaysia, Thailand, Vietnam
        *   East Asia: China, Japan, South Korea
        *   South Asia: Bangladesh, India, Sri Lanka
        *   North America: USA
        *   Europe: UK
    *   `PolicyType` (Policies): "Whole Life", "Endowment", "Term", "Investment-Linked (SP)", "Investment-Linked (RP)", "Hospital & Surgical", "Long Term Care", "Personal Accident", "Critical Illness", "Universal Life (Traditional)", "Universal Life (Indexed)", "Universal Life (Variable)", "PPLI".
    *   `InsuranceProvider` (Policies): "AIA", "China Life", "China Taiping", "Great Eastern", "Prudential", "Manulife", "Income", "Singlife", "AXA", "HSBC Life", "Sun Life", "Tokio Marine", "Transamerica". *Default to blank or first entry.*
    *   `PremiumFrequency` (Policies): "Annually", "Semi-Annually", "Quarterly", "Monthly", "Single Premium".
    *   `PaymentMode` (Policies): "GIRO", "Credit Card", "Internet Banking", "AXS", "Cheque", "Cash".
    *   `BenefitLevel` (Coverages): "Main Plan", "Rider".
    *   `CoverageType` (Coverages): "Death", "TPD" (Total Permanent Disability), "CI" (Critical Illness), "ECI" (Early Critical Illness), "H&S" (Hospital & Surgical), "LTC" (Long Term Care), "Premium Waiver", "PA" (Personal Accident), "Acc Death" (Accidental Death), "Hospital Cash - Daily", "Hospital Cash - Weekly".

*   **Calculated Field (Not Stored in DB):**
    *   `Annualised_Premium` (Policies): Calculated in application logic (backend/frontend) as `PremiumAmount * FrequencyMultiplier`. Frequency Multipliers: Annually=1, Semi-Annually=2, Quarterly=4, Monthly=12. Handle 'Single Premium' appropriately (Multiplier=1, or display logic might differ).


## 5. Technology Stack (Proposed/Requested)

Given the goal of straightforward implementation and compatibility with Replit's environment, the following technology stack is preferred:

*   **Frontend (UI):**
    *   **Chosen:** **HTML, CSS, and Vanilla JavaScript (Option 1)**.
    *   **Reasoning:** Avoids framework overhead for simpler generation and modification. Focus on clean HTML, standard CSS (Flexbox/Grid for layout/responsiveness), and plain JavaScript for interactivity (forms, validation, dynamic rows, API calls, calculations, UI logic).
*   **Backend (Logic/Data Handling):**
    *   **Chosen:** **Python with the Flask framework (Option 1)**.
    *   **Reasoning:** Well-supported on Replit, beginner-friendly, sufficient for API endpoints (CRUD operations), calculations, and database interaction.
*   **Database:**
    *   **Chosen:** **SQLite (Recommendation Accepted)**.
    *   **Reasoning:** Ideal for local use and NAS migration (single file, serverless). The database file (e.g., `client_data.db`) should reside within the project directory.


## 6. Development & Deployment Plan

*   **Phase 1: Initial Development & Local Use (Now - 6 Months):**
    *   **Environment:** Primary development and testing within Replit. Application runnable directly on local machines (Windows, macOS) for testing/initial use.
    *   **Goal:** Achieve a stable, functional version covering all core features, suitable for personal use from a local hard drive.
    *   **Database Location:** SQLite database file (`client_data.db`) stored within the project's main directory.

*   **Phase 2: NAS Migration & Deployment (Target: ~6 Months):**
    *   **Goal:** Migrate the application and database for operation from a personal NAS.
    *   **Approach:** Copy application folder (including `client_data.db`) to NAS. Ensure Python/Flask can run on NAS. Run Flask backend on NAS. Access UI via browser over local network to NAS IP/port.
    *   **Consideration:** Design should not hinder file-based deployment. No external dependencies needed for core functionality.


## 7. Additional Notes / Preferences

*   Error handling should be user-friendly (clear messages, avoid technical jargon where possible).
*   Prioritize data integrity and validation on both frontend and backend.
*   Keep the initial setup and running process simple.
*   Ensure UI responsiveness across common desktop and tablet screen sizes.
