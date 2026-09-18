# Ganesh Tech — Living Spec

## Product
Ganesh Tech is a premium single-page IT company website for enterprise buyers. It presents infrastructure, cybersecurity, cloud, AI, software development, and digital transformation services with a dark futuristic visual system and responsive sections.

## Data model
- `Enquiry`: `id`, `full_name`, `company`, `email`, `phone`, `service_required`, `message`, `reference_number`, `created_at`
- Enquiries are stored in MongoDB collection `enquiries` and receive a human-readable `ZZZOR-XXXX` reference number.

## Key flows
1. Visitors move between anchored Home, About, Services, Solutions, Industries, Technologies, Projects, and Contact sections.
2. Visitors submit the Contact form; the frontend calls `POST /api/enquiries`, shows a success state with the reference number, and resets the form.
3. The navigation and CTA buttons scroll to relevant sections; the mobile menu collapses after navigation.

## Auth and roles
There is no authentication or gated area. The enquiry form is public.

## Integrations
No external email, CRM, payment, or AI integration is configured. Enquiries are stored in the app database only.