---
fonte: https://support.google.com/appsheet/answer/11917548?hl=en
baixado: 2026-11-10
---

# HIPAA implementation guide

Ensuring that our customers' data is safe, secure, and available to them is one of our top priorities. For customers who are subject to the requirements of the Health Insurance Portability and Accountability Act (HIPAA), AppSheet can also support HIPAA compliance as a business associate (as the term is defined in HIPAA). This HIPAA Implementation Guide is intended to help you configure the data you send to AppSheet in light of the way our services work and the sensitivity of protected health information.

Under HIPAA, certain information about a person’s health or health care services is classified as Protected Health Information (PHI). AppSheet customers who are subject to HIPAA and wish to use AppSheet with PHI must sign a Business Associate Agreement (BAA) before any such information can be used with AppSheet.

Please note that this HIPAA Implementation Guide is provided by Google solely as an informational guide with respect to your configuration options. AppSheet customers are ultimately responsible for determining whether they are subject to HIPAA requirements and whether they use or intend to use AppSheet services in connection with PHI. Customers are also responsible for ensuring that their use and their end users’ and app users’ use of the AppSheet Services complies with HIPAA and HITECH. Customers who have not signed a BAA with Google must not use Google services in connection with PHI.

Administrators must review and accept a BAA before using Google services with PHI.

For more information about signing a BAA, contact your [AppSheet Sales](https://cloud.google.com/contact/?direct=true&pre_product=appsheet) representative.

## Required configuration

### Configure PHI data as sensitive

AppSheet offers the ability to mark certain data in a customer's data store as sensitive, which obscures it in the audit logs. Any data subject to HIPAA processed with an AppSheet app must be marked as sensitive by the customer, as described in the [Sensitive Personally Identifiable Information (PII) Data Policy Manual](https://support.google.com/appsheet/answer/10104377).

### PHI in the app definitions

AppSheet customers are responsible for ensuring that no PHI is used in the app definition. Customers specify the app definition when they build their application through our website, for instance when they specify data sources to use, view names and associated metadata. The app definition will define how the app will look and work to its users.

### PHI in support tickets

AppSheet customers are responsible for ensuring that no PHI is submitted in the support tickets.
