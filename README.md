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
        *   **Sortable:** Allow sorting the client list (e.g., by `FullName`, `DateAdded`) through clear UI controls (e.g., clickable column headers or dedicated sort dropdowns).
    *   [ ] **Select & View Details:** Select a client from the list to view their full details (personal information and associated policies) in a dedicated view.
    *   [ ] **Update:** Edit and save changes to existing client information.
    *   [ ] **Delete:** Remove a client record. *(Note: Consider implications - deleting a client might require deleting associated policies or handling orphaned records. Soft delete/archiving might be safer long-term but adds complexity).*

*   **Policy Management (within a selected Client's context):**
    *   [ ] **Add:** Create new insurance policy records, ensuring each new policy is correctly linked to the currently viewed client.
    *   [ ] **List & View:** Display all policies associated with the selected client (e.g., using policy cards). This list should be:
        *   **Sortable:** Allow sorting the policies (e.g., by `PolicyType`, `InceptionDate`, `PolicyNumber`) through clear UI controls.
    *   [ ] **Select & View Details:** Select a policy... displaying its details and associated coverages in the two-card layout.
    *   [ ] **Update:** Edit and save changes to existing policy information *and its associated coverages*.
    *   [ ] **Delete:** Remove a policy record *and all its associated coverage records*.
    *   [ ] **Manage Policy Coverages:** Within the policy edit view, allow users to add, view, update, and delete individual coverage lines using the dynamic row interface ("+" / "-" buttons).
    *   [ ] **Calculate & Display:** Automatically calculate and display the `Annualised_Premium` based on `PremiumAmount` and `PremiumFrequency` in the Policy Details card.

*   **Search & Data Retrieval:**
    *   [ ] Implement the global **Search Bar** in the header for quick client lookup (`FullName`, `Personal_ID`) and potentially policy lookup (`PolicyNumber`).

*   **Reporting & Visualization (Using Chart.js and potentially Leaflet):**
    *   [ ] **Business Portfolio Visualization (in dedicated 'Reports' view/component):**
        *   **a. Gender Distribution:** Display client count by `Gender`. (Backend: `GET /api/reports/gender_distribution`, SQL `GROUP BY Gender`. Frontend: Pie chart).
        *   **b. Insurance Provider Distribution:** Display policy count by `InsuranceProvider`. (Backend: `GET /api/reports/provider_distribution`, SQL `GROUP BY InsuranceProvider`. Frontend: Bar chart, potentially vertical).
        *   **c. Policy Type Distribution:** Display policy count by `PolicyType`. (Backend: `GET /api/reports/policy_type_distribution`, SQL `GROUP BY PolicyType`. Frontend: donut chart).
        *   **d. Geographical Distribution (Singapore):** Display client count concentration by Postal Sector on an interactive map of Singapore. (Backend: `GET /api/reports/geo_distribution_sg`, SQL `GROUP BY SUBSTR(Res_Postal_Code, 1, 2)`. Frontend: Choropleth map using Leaflet/Vue-Leaflet and Singapore GeoJSON data. *Note: High complexity, potential deferral.*).
    *   [ ] **Client Portfolio Visualization (within 'Client Detail' view/component):**
        *   **a. Policies by Provider:** Display policy count grouped by `InsuranceProvider` for the selected client. (Backend: Data derived from existing `/api/clients/<id>` response. Frontend: Pie chart using client's policy data).
        *   **b. Policies by Policy Type:** Display policy count grouped by `PolicyType` for the selected client. (Backend: Data derived from existing `/api/clients/<id>` response. Frontend: Pie or Bar chart using client's policy data).
        *   **c. Benefits by Type (Sum Assured):** Display total `CoverageSumAssured` grouped by `CoverageType` for the selected client. (Backend: `GET /api/reports/client/<id>/benefit_sum_assured`, SQL `GROUP BY CoverageType, SUM(CoverageSumAssured)`. Frontend: Bar chart).
        *   **d. Benefit End Age vs. Sum Assured:** Display coverage end age vs. sum assured for the selected client. (Backend: `GET /api/reports/client/<id>/benefit_end_age`, Calculate End Age from `CoverageTillAge` or `MaturityExpiryDate - DOB`. Frontend: Multi-line chart using Plotly.js, mapping End Age (x) vs. Sum Assured (y), potentially color-coded by `CoverageType`).

*   **Data Handling & Persistence:**
    *   [ ] **Persistence:** Reliably save all client, policy, and coverage data to the designated database (SQLite file initially).
    *   [ ] **Validation:** Implement input validation based on the defined database schema (e.g., ensure required fields are filled, data types match like valid dates/email formats, numeric fields contain numbers). Provide user-friendly error messages for validation failures, preferably next to the invalid field.


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
    *   **Primary Navigation:** Implement a **vertical sidebar** on the left side for main application sections (e.g., 'Dashboard/Overview', 'Clients', 'Reports', 'Settings'). This provides a clear hierarchy and is space-efficient for content areas. Contains clickable links/elements for navigation (using Vue Router).
    *   **Header:** Utilize a **sticky/fixed header** at the top of the page. This ensures consistent access to key functions regardless of scroll position.
    *   **Search:** Include a **prominent search bar** within the sticky header for efficient data retrieval as defined in Core Features.
    *   **Content Area:** The main area to the right of the sidebar and below the header will display the core content (client lists, forms, dashboards, reports). This area will dynamically change based on the selected view/navigation managed by Vue Router.
    *   **Breadcrumbs:** Implement breadcrumbs, likely displayed below the header or at the top of the content area, to show the user's current location within the application's hierarchy (e.g., `Home > Clients > [Client Name] > Edit Policy`).

*   **Content Display & Interaction:**
    *   **Component-Based Approach:** The UI should be built using logical Vue.js components (e.g., ClientListCard, ClientDetailForm, PolicyCard, CoverageRow, BasePieChart, BaseBarChart, MapComponent).
    *   **Card-Based Layout:** Use a **card-based layout** within the main content area to segment and display lists of items clearly (e.g., Client list uses summary cards, a Client's Policies view shows policy cards). Consider a grid layout for these cards where appropriate.
    *   **Forms:** Data entry forms should be well-structured within components, using clear labels, logical grouping of fields, and appropriate input controls (text fields, date pickers, dropdowns, etc.). When a form is loaded, automatically set the keyboard focus to the first input field.
        *   **Personal Information Layout:** Within the component displaying the client's main personal details, arrange fields in a **two-column grid** (stacking vertically on mobile) as specified previously (Salutation, Full Name, ID, DOB, Gender, Marital Status in Col1; Smoking, Occupation, Income, Mobile, Email in Col2).
        *   **Address Layouts:** The Residential and Mailing Address components should each use the specified **two-column grid** layout (Block/House, Street in Col1; Unit, Postal, Country in Col2), stacking vertically on mobile. Implement the "Mailing Address same as Residential" checkbox logic to conditionally display/manage the Mailing Address component/fields.
        *   **Specific Controls:** Use appropriate HTML controls or framework-specific components for inputs: Radio buttons (Gender, Salutation, etc.), Dropdowns (Country, PolicyType, etc.), Date pickers (display DD/MM/YYYY), Checkbox (MailingSameAsResidential).
    *   **Transitions & Feedback:** Implement **smooth transitions and subtle animations** where appropriate (e.g., view changes, loading states, expanding details). Provide clear visual feedback for user actions (button clicks, saves, errors). Display clear loading indicators (e.g., spinners, placeholders) when fetching data or saving data.
    *   **Policy View Layout:** When viewing/editing a specific policy, use two main components/cards:
        *   **Card 1: "Policy Details Component":** Displays/allows editing of fields from the `Policies` table. Shows calculated `Annualised_Premium`.
        *   **Card 2: "Policy Coverages Component":** Displays associated coverages in a table-like structure or repeating rows/components.
            *   Layout within each coverage row/component should attempt a single-line format, wrapping on mobile.
            *   **Dynamic Row Management:** Include functional "+" and "-" buttons to add/remove coverage rows/components dynamically, updating the underlying data model.
    *   **Visualization Display:**
        *   Business-level charts (Pie, Bar, Map) will be displayed within the dedicated `Reports` view component.
        *   Client-level charts (Pie, Bar, Scatter) will be displayed within the `Client Detail` view component, likely in a dedicated section or tab within that view.

*   **Key Design Principles:**
    *   **Consistency:** Maintain a consistent design language (colors, typography, component styles, interaction patterns) throughout the application.
    *   **Accessibility:** Ensure the UI is accessible. Use clear labels, sufficient color contrast, appropriate spacing, and keyboard navigability where feasible. Follow standard accessibility guidelines (WCAG).

*   **Responsiveness & Cross-Platform:**
    *   **Mobile Optimization:** The web UI *must* be responsive and adapt gracefully to different screen sizes, including tablets (iPadOS) and potentially smaller mobile viewports. For smaller screens, the vertical sidebar might collapse into a hamburger menu, and horizontal layouts may need to stack vertically.

## 4. Data Structure / Database Schema

*   **Database Integrity:** The backend database connection (using Python/Flask) **must** enable foreign key constraint enforcement in SQLite (e.g., using `PRAGMA foreign_keys = ON;` upon connection).

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

Given the interactive nature of the UI (multiple views, dynamic forms, state management between client/policy views) and aiming for a balance between modern structure and implementation feasibility with AI assistance:

*   **Frontend (UI):**
    *   **Chosen:** **Vue.js (using Vue 3 Composition API and `<script setup>`)**
    *   **Reasoning:** Provides essential structure for component-based UI, reactive state management, and conditional rendering, making generation of a functional and maintainable application more feasible via AI compared to Vanilla JS.
    *   **Build Tool:** Use **Vite** for project setup and development server (provides fast HMR).
    *   **Routing:** Use **Vue Router** for managing navigation between different application views.
    *   **UI Components (Optional):** Consider using a simple Vue component library like **PrimeVue** or **Element Plus** for pre-built components, OR rely on custom styling with CSS. *Specify preference if any.*
    *   **Charting Library:** Include **Chart.js** and a Vue wrapper (like **`vue-chartjs`**) for visualizations (Section 2).
    *   **Mapping Library (Optional):** For geographical visualization, **Leaflet** with a Vue wrapper (like **`vue-leaflet`**) is needed. Requires separate GeoJSON data.
*   **Backend (Logic/Data Handling):**
    *   **Chosen:** **Python with the Flask framework (Option 1)**.
    *   **Reasoning:** Well-supported on Replit, relatively simple, sufficient for creating the necessary RESTful API endpoints.
*   **Database:**
    *   **Chosen:** **SQLite (Recommendation Accepted)**.
    *   **Reasoning:** Ideal for local use and NAS migration (single file, serverless). The database file (e.g., `client_data.db`) should reside within the backend's project directory.


## 6. Development & Deployment Plan

*   **Phase 1: Initial Development & Local Use (Now - 6 Months):**
    *   **Environment:** Primary development and testing within Replit. Application runnable directly on local machines (Windows, macOS) for testing/initial use (requires Node.js/npm for frontend build/dev server, Python for backend).
    *   **Goal:** Achieve a stable, functional version covering all core features, suitable for personal use from a local hard drive.
    *   **Database Location:** SQLite database file (`client_data.db`) stored within the backend's project directory.

*   **Phase 2: NAS Migration & Deployment (Target: ~6 Months):**
    *   **Goal:** Migrate the application and database for operation from a personal NAS.
    *   **Approach:**
        *   Backend: Copy backend Python/Flask code and `client_data.db` to NAS. Ensure Python/Flask can run. Run Flask backend on NAS.
        *   Frontend: Build the Vue.js application for production (`npm run build`). Copy the resulting static files (HTML, CSS, JS from the `dist` folder) to be served by the NAS (either via Flask itself configured to serve static files, or a separate web server like Nginx/Apache on the NAS).
        *   Access UI via browser over local network to NAS IP/port.
    *   **Consideration:** Design should not hinder deployment. Backend API should be accessible from the frontend build.


## 7. Additional Notes / Preferences

*   Error handling should be user-friendly (clear messages, avoid technical jargon where possible).
*   Prioritize data integrity and validation on both frontend (initial checks) and backend (authoritative checks).
*   Keep the initial setup and running process simple (provide clear instructions if using Vite/npm).
*   Ensure UI responsiveness across common desktop and tablet screen sizes.
*   **Incremental Build Recommended:** Even with Vue.js, prompt the AI to build features incrementally (e.g., setup, backend endpoints first, then frontend components one by one). Test each part thoroughly.
*   **API Communication:** Ensure clear communication patterns between the Vue.js frontend and the Flask backend API (using `fetch` or libraries like `axios`).
*   **Geographical Map Complexity:** Implementing the Singapore map visualization (Feature 2.d) requires significant extra effort involving GeoJSON data sourcing/processing and integrating a mapping library (Leaflet); consider this an advanced feature or potential deferral.
