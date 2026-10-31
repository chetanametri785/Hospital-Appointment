# MediCare Plus - Hospital Appointment Booking & Status Portal

A modern, responsive, healthcare web application featuring an elegant **blue and white** clinical theme. It allows patients to book specialist doctor consultations and track their live appointment status, queue tokens, room numbers, and clinical preparation instructions in real time.

Built to run effortlessly inside **Visual Studio Code**.

---

## ✨ Features

- **Clinical Blue & White Theme**: Professional, clean, accessible medical aesthetic with custom SVG icons, soft shadows, responsive grids, and subtle status animations.
- **Interactive Multi-Step Booking**:
  - **Step 1: Patient Information**: Name, phone, email, age, gender, blood group, symptoms description, and consultation type (OPD, Video Call, Routine Follow-up).
  - **Step 2: Department & Doctor Selection**: 8 clinical specialties (Cardiology, Neurology, Pediatrics, Orthopedics, General Medicine, Dermatology, Ophthalmology, Gynecology) and 8+ board-certified specialist profiles with live fees, credentials, and room allocations.
  - **Step 3: Date & Time Slot Picker**: Minimum date protection, morning, afternoon, and evening slot pills.
  - **Live Consultation Summary Sidebar**: Real-time feedback of patient choices and fee breakdown.
  - **Instant Digital Token Generation**: Generates unique appointment IDs (e.g. `MC-8491`), queue tokens (`T-12`), and assigns OPD rooms automatically.
- **Real-Time Booking Status Tracker**:
  - Search by Appointment Reference ID (e.g. `MC-1001`), patient phone number, or email.
  - Quick clickable demo chips (`MC-1001`, `MC-1002`, `MC-1003`, `MC-1004`, `MC-1005`) for immediate testing of all statuses.
  - **Visual 5-Stage Stepper / Progress Timeline**:
    1. Requested (Booked Online)
    2. Desk Review (Verification)
    3. Confirmed (Token & Room Ready)
    4. In-Consultation (With Doctor)
    5. Completed (Prescription Issued)
    *(Also includes real-time Cancelled flow)*
  - **Patient Actions**:
    - 🔄 **Reschedule Appointment**: Change date and slot dynamically with instant history log.
    - ❌ **Cancel Appointment**: Instant cancellation with slot release and timeline update.
    - 🖨️ **Print Official Slip**: Clean print layout with dedicated `@media print` styles.
- **Hospital Administration & Reception Desk**:
  - Summary KPI cards: Total Bookings, Confirmed, Pending Approvals, Today's Consultations.
  - Filter bookings by status: `All`, `Pending`, `Confirmed`, `In-Progress`, `Completed`, `Cancelled`.
  - Search filter by patient name, doctor, or ID.
  - Reception action buttons to **Confirm** appointments, **Check-In** patients, mark **Completed**, or **Cancel**.
  - **Reset Demo Data** button to quickly restore sample appointments at any time.
- **Specialist Doctors Directory**: Browse departments and doctors with a 1-click **"Book Consultation"** shortcut that pre-selects the doctor in the booking form.
- **24/7 Emergency Response Banner & Interactive FAQs**: Hotline quick dial and accordion questions.
- **Zero External Dependencies**: Pure HTML5, CSS3, JavaScript, and Node.js.

---

## 🚀 How to Run in VS Code

You can run this project in VS Code using any of the three simple methods below:

### Method 1: Using the Node.js Server (Recommended)
1. Open the project folder in **Visual Studio Code** (`File` -> `Open Folder...`).
2. Open the integrated terminal (`Ctrl + ~` or `Terminal` -> `New Terminal`).
3. Run:
   ```bash
   node server.js
   ```
   *(or `npm start`)*
4. Open your web browser and visit:
   ```
   http://localhost:3000
   ```

### Method 2: Press F5 (VS Code Run & Debug)
1. Open the project folder in **VS Code**.
2. Press **`F5`** (or go to `Run` -> `Start Debugging`).
3. The server starts automatically using the pre-configured `.vscode/launch.json` file.
4. Open `http://localhost:3000` in your browser.

### Method 3: Using the VS Code Live Server Extension
1. Install the **Live Server** extension in VS Code (by *Ritwick Dey*).
2. Right-click on `index.html` in the file explorer.
3. Select **"Open with Live Server"**.
4. The website will open at `http://127.0.0.1:5500/index.html`.

---

## 📁 File Structure

```text
20 Project/
├── .vscode/
│   ├── launch.json       # VS Code Node.js launch configuration (F5)
│   └── settings.json     # VS Code workspace settings (Live Server configuration)
├── css/
│   └── styles.css        # Clinical blue & white styling, animations, responsive & print media queries
├── js/
│   ├── data.js           # Departments, doctors, seed appointments, and hospital info
│   └── app.js            # Booking wizard, status tracker, admin portal, and toast system
├── index.html            # Main website entry point
├── package.json          # Node.js project manifest
├── server.js             # Zero-dependency local Node.js HTTP web server
└── README.md             # Project documentation and user guide
```

---

## 🧪 Sample Appointment IDs for Testing

Click or enter any of these sample reference IDs in the **Check Status** section:
- **`MC-1001`**: Sophia Martinez - **Confirmed** (Cardiology, Token `T-08`, Room 304)
- **`MC-1002`**: James Harrison - **Pending** (Orthopedics, Awaiting desk verification)
- **`MC-1003`**: Liam Johnson - **In-Progress** (Pediatrics, Currently with Dr. Jenkins)
- **`MC-1004`**: Elena Rostova - **Completed** (Dermatology, Teleconsultation finished)
- **`MC-1005`**: Arthur Miller - **Cancelled** (General Medicine, Slot released)
