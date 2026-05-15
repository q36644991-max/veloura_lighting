# Product Requirements Document (PRD)
# Veloura Lighting

## Tagline
"Illuminating Luxury Spaces."

---

# 1. Project Overview

## Product Name
Veloura Lighting

## Product Type
Luxury Interior Lighting Design & Premium Lighting Showcase Website

## Purpose
Veloura Lighting is a premium luxury lighting brand focused on:
- interior lighting design
- luxury lighting products
- ambient architectural lighting
- premium consultation services

The website will serve as:
- a luxury digital showroom
- a portfolio platform
- a lead generation platform
- a premium brand identity website

The overall experience should feel:
- luxurious
- cinematic
- warm
- elegant
- modern
- immersive

---

# 2. Business Goals

## Primary Goals
- Generate high-quality luxury client leads
- Showcase premium lighting collections
- Build strong luxury brand identity
- Increase consultation bookings
- Establish online authority in luxury lighting

## Secondary Goals
- Display completed interior projects
- Create trust with architects/interior designers
- Expand future e-commerce capabilities

---

# 3. Target Audience

## Primary Audience
- Luxury homeowners
- Interior designers
- Architects
- Villa owners
- Hotel & resort businesses
- Premium commercial spaces

## Secondary Audience
- Smart home customers
- Real estate developers
- High-end renovation clients

---

# 4. Brand Identity

## Brand Personality
- Sophisticated
- Warm
- Minimal
- Premium
- Artistic

---

# 5. Design System

## Color Palette

| Purpose | Color | Hex |
|---|---|---|
| Main Background | Deep Forest Green | #0F2A24 |
| Secondary Background | Emerald Green | #163832 |
| Accent Gold | Luxury Gold | #D4AF37 |
| Warm Highlight | Candle Yellow | #F4C95D |
| Primary Text | Ivory White | #F8F5EE |
| Secondary Text | Soft Beige | #C8BFAF |

---

# 6. Typography

## Heading Fonts
- Playfair Display
- Cinzel

## Body Fonts
- Inter
- Manrope

---

# 7. Tech Stack

## Frontend
- HTML5
- Tailwind CSS (CDN)
- Vanilla JavaScript

## Backend
- Python Flask
- Microservice Architecture

## Database & Authentication
- Supabase

## Deployment
Frontend:
- Vercel

Backend:
- Render

---

# 8. Website Features

## Public Website Features

### Home Page
Purpose:
- Introduce brand identity
- Create luxury visual impact

Sections:
- Cinematic Hero Banner
- Featured Luxury Collections
- Premium Lighting Categories
- Featured Projects
- Brand Story
- Testimonials
- Consultation CTA
- Footer

---

### About Page
Features:
- Company story
- Brand vision
- Design story
- Team introduction

---

### Collections Page
Purpose:
Showcase luxury lighting products.

Features:
- Product grid
- Filtering system
- Search functionality
- Product categories
- Quick preview modal

Categories:
- Chandeliers
- Pendant Lights
- Smart Lighting
- Wall Lights
- Decorative Lamps
- Outdoor Luxury Lighting

---

### Product Details Page
Features:
- High-resolution gallery
- Product specifications
- Lighting tone indicators
- Inquiry button
- Material information
- Luxury presentation layout

---

### Portfolio Page
Purpose:
Display completed lighting projects.

Features:
- Project galleries
- Before/After visuals
- Interior case studies
- Luxury design showcases

Project Categories:
- Villas
- Apartments
- Hotels
- Commercial Spaces

---

### Consultation Booking Page
Features:
- Booking form
- Project requirement form
- Preferred consultation schedule
- Contact details submission

---

### Contact Page
Features:
- Contact form
- Business location
- Google Maps integration
- WhatsApp CTA
- Social media links

---

# 9. Admin Dashboard

## Features

### Product Management
- Add/Edit/Delete products
- Upload product images
- Manage pricing
- Manage categories

### Portfolio Management
- Upload project galleries
- Edit project details

### Booking Management
- View consultation requests
- Manage leads

### Analytics
- Product views
- Website visits
- Inquiry tracking

---

# 10. Functional Requirements

## Authentication
- Secure admin login
- JWT authentication
- Protected routes

---

## Product Management System
- CRUD operations
- Image upload support
- Category filtering
- Search support

---

## Booking System
- Consultation request form
- Email notifications
- Admin management panel

---

## Portfolio System
- Gallery uploads
- Responsive image handling
- Project categorization

---

# 11. Non-Functional Requirements

## Performance
- Fast loading speed
- Optimized images
- Lazy loading implementation

## Responsiveness
- Mobile-first UI
- Tablet optimized
- Desktop optimized

## Security
- HTTPS encryption
- API protection
- Secure authentication

## SEO
- Meta optimization
- Search engine indexing
- Structured metadata

---

# 12. Backend Architecture

## Microservice Structure

/backend
    /gateway
    /auth-service
    /product-service
    /booking-service
    /portfolio-service
    /email-service

---

# 13. Database Schema

## users

id
name
email
password
role
created_at

---

## products

id
name
description
price
category
image_url
stock
created_at

---

## projects

id
title
description
category
image_urls
created_at

---

## bookings

id
name
email
phone
project_type
message
booking_date
created_at

---

## testimonials

id
client_name
review
rating
created_at

---

# 14. UI/UX Requirements

## Visual Direction
The UI should feel:
- luxurious
- warm
- cinematic
- minimal
- premium

---

## UI Effects
- Smooth scrolling
- Golden hover glow
- Ambient lighting gradients
- Fade-in animations
- Elegant page transitions
- Soft glassmorphism cards

---

# 15. API Endpoints

## Product APIs

GET /products
POST /products
PUT /products/<id>
DELETE /products/<id>

---

## Booking APIs

POST /bookings
GET /bookings

---

## Portfolio APIs

GET /projects
POST /projects

---

# 16. Future Enhancements

## Planned Features
- AI lighting recommendations
- AR lighting preview
- Smart home integration
- Online payments
- Wishlist system
- Customer login portal

---

# 17. Success Metrics

## KPIs
- Monthly inquiries
- Consultation bookings
- Product engagement
- Portfolio page traffic
- Conversion rates
- Average session duration

---

# 18. Final Vision

Veloura Lighting should feel like:
- a premium architectural lighting brand
- a luxury digital showroom
- an immersive interior lighting experience

The website should emotionally communicate:
"elegance, warmth, luxury, sophistication, and timeless illumination."