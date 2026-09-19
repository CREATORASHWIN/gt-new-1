# Ganesh Tech — Living Spec

## Product
Ganesh Tech is a premium single-page IT company website for enterprise buyers. It presents nine service lines spanning infrastructure, cybersecurity, cloud, AI, software, transformation, managed IT, data and analytics, and business continuity with a dark futuristic visual system and responsive sections.

## Data model
- `Enquiry`: `id`, `full_name`, `company`, `email`, `phone`, `service_required`, `message`, `reference_number`, `created_at`
- Enquiries are stored in MongoDB collection `enquiries` and receive a human-readable `ZZZOR-XXXX` reference number.

## Key flows
1. Visitors move between anchored Home, About, Services, Solutions, Industries, Technologies, Projects, and Contact sections.
2. Visitors submit the Contact form; the frontend calls `POST /api/enquiries`, shows a success state with the reference number, and resets the form.
3. The navigation and CTA buttons scroll to relevant sections; the mobile menu collapses after navigation.
4. Every service card opens a detailed brief with its overview, deliverables, business outcomes, and a prefilled enquiry action.
5. Every technology category opens a capabilities panel with platforms, practices, and best-fit use cases.
6. Every project card opens a full case-study brief with challenge, solution, implementation, results, and a prefilled project enquiry action.
7. The hero network sphere rotates about 27% faster than the original version, with continuous GPU-friendly rotation, restrained float, and a smaller mobile composition.
8. The Industries section uses a desktop hover/focus selector with a large active 3D system visual and a separate mobile tap-to-expand card experience for all nine industries.
9. The mobile navigation is a full-height animated menu that locks background scrolling and closes after section selection.

## Auth and roles
There is no authentication or gated area. The enquiry form is public.

## Integrations
No external email, CRM, payment, or AI integration is configured. Enquiries are stored in the app database only.