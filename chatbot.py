# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 12:22:30 2025

@author: zhi yan
"""
# -*- coding: utf-8 -*-
"""
Jewel Changi Airport FAQ System
Created on Wed Jul 23 12:22:30 2025
@author: zhi yan
"""
from difflib import get_close_matches

class JewelChangiFAQ:
    def __init__(self):
        self.faq = {
            "opening hours": self._opening_hours_response(),
            "ticket prices": self._ticket_prices_response(),
            "birthday party": self._birthday_party_response(),
            "singapore deal": self._singapore_deal_response(),
            "contact": self._contact_response(),
            "bulk discount": self._bulk_discount_response(),
            "attractions": self._attractions_response(),
            "is it cheaper to buy in bulk": self._bulk_discount_response(),
            "what can i do at jewel changi": self._attractions_response(),
            "how to get there": self._transport_response(),
            "restaurants": self._dining_response(),
            "shops": self._shopping_response(),
            "learning journey": self._learning_journey_response(),
            "team bonding": self._team_bonding_response(),
            "venue rental": self._venue_rental_response(),
            "school program": self._learning_journey_response(),
            "corporate event": self._team_bonding_response(),
            "private event": self._venue_rental_response(),
            "what is changi experience studio": self._ces_info_response(),
            "ces facilities": self._ces_facilities_response(),
            "ces activities": self._ces_activities_response(),
            "changi experience studio tickets": self._ticket_prices_response(),
            "ces operating hours": self._opening_hours_response()
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        # Map variations to standard questions
        question_map = {
            'bulk': 'bulk discount',
            'attraction': 'attractions',
            'things to do': 'attractions',
            'discount': 'bulk discount',
            'cheaper': 'bulk discount',
            'hours': 'opening hours',
            'time': 'opening hours',
            'open': 'opening hours',
            'price': 'ticket prices',
            'cost': 'ticket prices',
            'party': 'birthday party',
            'deal': 'singapore deal',
            'promo': 'singapore deal',
            'contact': 'contact',
            'phone': 'contact',
            'email': 'contact',
            'transport': 'how to get there',
            'directions': 'how to get there',
            'mrt': 'how to get there',
            'bus': 'how to get there',
            'eat': 'restaurants',
            'food': 'restaurants',
            'dining': 'restaurants',
            'shop': 'shops',
            'shopping': 'shops',
            'store': 'shops',
            'learn': 'learning journey',
            'school': 'learning journey',
            'education': 'learning journey',
            'team': 'team bonding',
            'corporate': 'team bonding',
            'company': 'team bonding',
            'venue': 'venue rental',
            'rent': 'venue rental',
            'private': 'venue rental',
            'event': 'venue rental',
            'facility': 'ces facilities',
            'facilities': 'ces facilities',
            'activity': 'ces activities',
            'activities': 'ces activities',
            'changi experience studio': 'what is changi experience studio',
            'ces': 'what is changi experience studio'
        }
        
        # Check for mapped terms
        for term, response_key in question_map.items():
            if term in user_input:
                return self.faq[response_key]
        
        # Check greetings
        greetings = ['hello', 'hi', 'hey', 'greetings']
        if any(greet in user_input for greet in greetings):
            return self._welcome_response()
        
        # Check thanks
        thanks = ['thank', 'thanks', 'appreciate']
        if any(t in user_input for t in thanks):
            return self._thank_you_response()
        
        # Check specific questions
        matches = get_close_matches(user_input, self.faq.keys(), n=1, cutoff=0.6)
        if matches:
            return self.faq[matches[0]]
        
        # Default response for unknown questions
        return self._unknown_question_response()

    def _welcome_response(self):
        return """<div class="response-box">
            <h3>Welcome to Jewel Changi Airport! ✈️</h3>
            <p>How can I help you today? Try asking about:</p>
            <div class="quick-options">
                <button class="quick-btn" onclick="askQuestion('opening hours')">⏰ Hours</button>
                <button class="quick-btn" onclick="askQuestion('ticket prices')">🎟️ Tickets</button>
                <button class="quick-btn" onclick="askQuestion('singapore deal')">🇸🇬 SG60 Deal</button>
                <button class="quick-btn" onclick="askQuestion('birthday party')">🎂 Parties</button>
                <button class="quick-btn" onclick="askQuestion('learning journey')">🎓 Learning Journey</button>
                <button class="quick-btn" onclick="askQuestion('team bonding')">👔 Team Bonding</button>
            </div>
            <div class="animation-container">
                <div class="airplane">✈️</div>
            </div>
        </div>"""

    def _opening_hours_response(self):
        return """<div class="response-box">
            <h3>⏰ Opening Hours</h3>
            <p><strong>Changi Experience Studio:</strong></p>
            <p>Mon-Fri: 11AM-8PM (last entry 7PM)</p>
            <p>Weekends/PH: 10AM-8PM (last entry 7PM)</p>
            
            <p><strong>Jewel Changi:</strong> Open 24 hours</p>
            <p>Shops typically 10AM-10PM</p>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/attractions/ces.html" class="action-button">🔗 Official Info</a>
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Enquiry Form</a>
            </div>
        </div>"""

    def _ticket_prices_response(self):
        return """<div class="response-box">
            <h3>🎟️ Ticket Prices & Packages</h3>
            
            <div class="deal-banner">
                <strong>🇸🇬 Singapore Residents Special!</strong> Ask about our "singapore deal"
            </div>
            
            <table class="price-table">
                <tr><th colspan="2">Changi Experience Studio</th></tr>
                <tr><td>Standard Adult</td><td>SGD 19.80</td></tr>
                <tr><td>Child/Senior/Student</td><td>SGD 14.80</td></tr>
                
                <tr><th colspan="2">Bundle Deals</th></tr>
                <tr><td>Bundle 3 (6 attractions)</td><td>SGD 56 (Adult) / SGD 40 (Child)</td></tr>
                <tr><td>Bundle 4 (7 attractions)</td><td>SGD 71 (Adult) / SGD 50 (Child)</td></tr>
                
                <tr><th colspan="2">Family Value Bundle</th></tr>
                <tr><td>2 Adults + 2 Children</td><td>SGD 59.80</td></tr>
            </table>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Book Now (All Deals)</a>
                <a href="https://tickets.jewelchangiairport.com/" class="action-button">ℹ️ Ticket Info</a>
            </div>
            
            <p class="note">ℹ️ Child: 5-12 years | Senior: 60+ years | Free for children below 5</p>
        </div>"""

    def _singapore_deal_response(self):
        return """<div class="response-box">
            <h3>🇸🇬 Singapore's 60th Birthday Deal</h3>
            
            <div class="deal-banner">
                <strong>Limited Time Offer!</strong> 6 tickets for S$60!
            </div>
            
            <p><strong>Promotion Details:</strong></p>
            <ul>
                <li>6 tickets for only S$60 (S$10 each)</li>
                <li>Seniors (60+ years): S$6 per ticket</li>
                <li>Valid: 14 Mar - 30 Sep 2025</li>
            </ul>
            
            <p><strong>Terms & Conditions:</strong></p>
            <ul>
                <li>Only available at Changi Experience Studio ticketing counter (Level 4)</li>
                <li>For Singapore residents only</li>
                <li>Must purchase in bundle of 6 tickets</li>
                <li>No refunds or exchanges</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Enquire Now</a>
                <a href="tel:+6569569898" class="action-button">📞 Call +65 6956 9898</a>
            </div>
        </div>"""

    def _birthday_party_response(self):
        return """<div class="response-box">
            <h3>🎂 Birthday Party Packages</h3>
            
            <table class="price-table">
                <tr><th>Package</th><th>Price</th><th>Inclusions</th></tr>
                <tr><td>Basic</td><td>SGD 380</td><td>10 children, 2hr venue, decorations</td></tr>
                <tr><td>Premium</td><td>SGD 550</td><td>15 children, 3hr venue, food options</td></tr>
                <tr><td>Deluxe</td><td>SGD 750</td><td>20 children, 4hr venue, full catering</td></tr>
            </table>
            
            <p><strong>Add-ons available:</strong></p>
            <ul>
                <li>Custom cakes: From SGD 50</li>
                <li>Goodie bags: From SGD 10 per child</li>
                <li>Photography services: From SGD 150</li>
                <li>Character mascot: From SGD 200</li>
            </ul>
            
            <p><strong>Available Time Slots:</strong></p>
            <ul>
                <li>Weekdays: 3PM-5PM or 5PM-7PM</li>
                <li>Weekends: 10AM-12PM, 1PM-3PM, or 4PM-6PM</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">🎈 Book Your Party</a>
                <a href="https://www.jewelchangiairport.com/en/attractions/ces.html" class="action-button">ℹ️ More Details</a>
            </div>
        </div>"""

    def _contact_response(self):
        return """<div class="response-box">
            <h3>📞 Contact Us</h3>
            
            <p><strong>Changi Experience Studio</strong><br>
            Level 4, Jewel Changi Airport</p>
            
            <p><strong>Operating Hours:</strong><br>
            11AM-8PM (Mon-Fri)<br>
            10AM-8PM (Weekends/PH)</p>
            
            <p><strong>Contact:</strong><br>
            ☎️ +65 6956 9898<br>
            ✉️ enquiries@jewelchangiairport.com</p>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 General Enquiry</a>
                <a href="https://www.jewelchangiairport.com/en/contact-us.html" class="action-button">🌐 More Options</a>
            </div>
        </div>"""

    def _bulk_discount_response(self):
        return """<div class="response-box">
            <h3>💰 Bulk Ticket Discounts</h3>
            <p>Yes! We offer several bulk purchase options:</p>
            
            <p><strong>1. Singapore 60th Birthday Special</strong></p>
            <ul>
                <li>6 tickets for S$60 (S$10 each)</li>
                <li>Available until 30 Sep 2025</li>
                <li>Counter purchase only</li>
            </ul>
            
            <p><strong>2. Family Value Bundle</strong></p>
            <ul>
                <li>2 Adults + 2 Children: S$59.80</li>
                <li>Saves ~20% off individual tickets</li>
            </ul>
            
            <p><strong>3. Group Bookings (10+ people)</strong></p>
            <ul>
                <li>Special rates for schools/companies</li>
                <li>Requires advance booking</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Enquire About Group Rates</a>
            </div>
        </div>"""

    def _attractions_response(self):
        return """<div class="response-box">
            <h3>🏆 Jewel Changi Attractions</h3>
            
            <p><strong>Main Attractions:</strong></p>
            <ul>
                <li><strong>Rain Vortex</strong> - World's tallest indoor waterfall</li>
                <li><strong>Canopy Park</strong> - Rooftop gardens & play attractions</li>
                <li><strong>Changi Experience Studio</strong> - Interactive digital attraction</li>
                <li><strong>Hedge Maze</strong> - Singapore's largest hedge maze</li>
                <li><strong>Mirror Maze</strong> - Unique mirror labyrinth</li>
            </ul>
            
            <p><strong>Featured Activities:</strong></p>
            <ul>
                <li>Walking Net & Bouncing Net (Canopy Park)</li>
                <li>Discovery Slides (Canopy Park)</li>
                <li>Mastercard® Canopy Bridge</li>
                <li>Foggy Bowls & Topiary Walk</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/attractions.html" class="action-button">🌐 View All Attractions</a>
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Package Enquiry</a>
            </div>
        </div>"""

    def _transport_response(self):
        return """<div class="response-box">
            <h3>🚍 How to Get to Jewel Changi</h3>
            
            <p><strong>By MRT:</strong></p>
            <ul>
                <li>Take East-West Line to Tanah Merah Station</li>
                <li>Transfer to Changi Airport Branch Line</li>
                <li>Alight at Changi Airport Station (CG2)</li>
                <li>Follow signs to Jewel</li>
            </ul>
            
            <p><strong>By Bus:</strong></p>
            <ul>
                <li>Bus services: 24, 27, 34, 36, 53, 110, 858</li>
                <li>Alight at Terminal 1, follow signs to Jewel</li>
            </ul>
            
            <p><strong>By Car/Taxi:</strong></p>
            <ul>
                <li>Address: 78 Airport Boulevard, Singapore 819666</li>
                <li>Parking available at Jewel (first hour free)</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/plan-your-visit/getting-here.html" class="action-button">🌐 Detailed Directions</a>
                <a href="https://www.changiairport.com/en/transport.html" class="action-button">🚖 Transport Options</a>
            </div>
        </div>"""

    def _dining_response(self):
        return """<div class="response-box">
            <h3>🍽️ Dining at Jewel Changi</h3>
            
            <p><strong>Popular Restaurants:</strong></p>
            <ul>
                <li><strong>Burger & Lobster</strong> - Seafood specialties</li>
                <li><strong>Shake Shack</strong> - Premium burgers</li>
                <li><strong>Paradise Dynasty</strong> - Chinese cuisine</li>
                <li><strong>Tonkotsu Kazan Ramen</strong> - Japanese ramen</li>
            </ul>
            
            <p><strong>Food Courts:</strong></p>
            <ul>
                <li><strong>Food Republic</strong> - Local hawker favorites</li>
                <li><strong>Five Spice</strong> - Asian street food</li>
            </ul>
            
            <p><strong>Opening Hours:</strong> Most F&B outlets open 10AM-10PM</p>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/dine.html" class="action-button">🌐 View All Dining Options</a>
                <a href="https://www.jewelchangiairport.com/en/whats-on/promotions.html" class="action-button">🍜 F&B Promotions</a>
            </div>
        </div>"""

    def _shopping_response(self):
        return """<div class="response-box">
            <h3>🛍️ Shopping at Jewel Changi</h3>
            
            <p><strong>Popular Stores:</strong></p>
            <ul>
                <li><strong>Naiise Iconic</strong> - Singapore souvenirs</li>
                <li><strong>Pokémon Center</strong> - Exclusive merchandise</li>
                <li><strong>Superdry</strong> - Fashion apparel</li>
                <li><strong>Tokyu Hands</strong> - Japanese lifestyle store</li>
            </ul>
            
            <p><strong>Specialty Shops:</strong></p>
            <ul>
                <li><strong>Bacha Coffee</strong> - Premium coffee</li>
                <li><strong>Irvins Salted Egg</strong> - Popular snacks</li>
                <li><strong>TWG Tea</strong> - Luxury tea boutique</li>
            </ul>
            
            <p><strong>Opening Hours:</strong> Most shops open 10AM-10PM</p>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/shop.html" class="action-button">🌐 View All Stores</a>
                <a href="https://www.jewelchangiairport.com/en/whats-on/promotions.html" class="action-button">🛒 Shopping Promotions</a>
            </div>
        </div>"""

    def _learning_journey_response(self):
        return """<div class="response-box">
            <h3>🎓 Learning Journey Programs</h3>
            
            <p>Changi Experience Studio offers immersive educational programs for schools:</p>
            
            <table class="price-table">
                <tr><th>Program</th><th>Duration</th><th>Price</th><th>Details</th></tr>
                <tr><td>Aviation Explorer</td><td>2 hours</td><td>SGD 15/student</td><td>Interactive aviation history</td></tr>
                <tr><td>Future Airport</td><td>3 hours</td><td>SGD 20/student</td><td>Technology & innovation in airports</td></tr>
                <tr><td>Singapore Stories</td><td>2.5 hours</td><td>SGD 18/student</td><td>Singapore's aviation journey</td></tr>
            </table>
            
            <p><strong>Program Features:</strong></p>
            <ul>
                <li>Curriculum-aligned content</li>
                <li>Interactive digital experiences</li>
                <li>Hands-on activities</li>
                <li>Certified educator guides</li>
            </ul>
            
            <p><strong>Group Requirements:</strong></p>
            <ul>
                <li>Minimum 15 students per group</li>
                <li>1 free teacher admission per 10 students</li>
                <li>Available weekdays only</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 School Enquiry</a>
                <a href="https://www.jewelchangiairport.com/en/attractions/ces.html" class="action-button">ℹ️ Program Details</a>
            </div>
        </div>"""

    def _team_bonding_response(self):
        return """<div class="response-box">
            <h3>👔 Corporate Team Bonding</h3>
            
            <p>Changi Experience Studio offers unique corporate team building programs:</p>
            
            <table class="price-table">
                <tr><th>Program</th><th>Duration</th><th>Price</th><th>Capacity</th></tr>
                <tr><td>Airport Challenge</td><td>2 hours</td><td>SGD 35/pax</td><td>15-50 pax</td></tr>
                <tr><td>Innovation Lab</td><td>3 hours</td><td>SGD 45/pax</td><td>10-30 pax</td></tr>
                <tr><td>Leadership Journey</td><td>4 hours</td><td>SGD 60/pax</td><td>10-25 pax</td></tr>
            </table>
            
            <p><strong>Program Features:</strong></p>
            <ul>
                <li>Customizable for your team needs</li>
                <li>Interactive challenges & simulations</li>
                <li>Debrief sessions with facilitators</li>
                <li>Catering options available</li>
            </ul>
            
            <p><strong>Available Time Slots:</strong></p>
            <ul>
                <li>Weekdays: 9AM-12PM or 2PM-5PM</li>
                <li>Weekends: Subject to availability</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Corporate Enquiry</a>
                <a href="tel:+6569569898" class="action-button">📞 Call for Custom Programs</a>
            </div>
        </div>"""

    def _venue_rental_response(self):
        return """<div class="response-box">
            <h3>🏛️ Venue Rental for Private Events</h3>
            
            <p>Changi Experience Studio offers unique spaces for private events:</p>
            
            <table class="price-table">
                <tr><th>Space</th><th>Capacity</th><th>Weekday Rate</th><th>Weekend Rate</th></tr>
                <tr><td>Digital Gallery</td><td>50 pax</td><td>SGD 1,200</td><td>SGD 1,800</td></tr>
                <tr><td>Innovation Lab</td><td>30 pax</td><td>SGD 900</td><td>SGD 1,350</td></tr>
                <tr><td>Full Studio</td><td>100 pax</td><td>SGD 2,500</td><td>SGD 3,800</td></tr>
            </table>
            
            <p><strong>Inclusions:</strong></p>
            <ul>
                <li>Basic AV equipment</li>
                <li>Standard setup</li>
                <li>2 staff assistants</li>
                <li>1 hour setup time</li>
            </ul>
            
            <p><strong>Available Add-ons:</strong></p>
            <ul>
                <li>Catering services</li>
                <li>Custom digital content</li>
                <li>Additional technical support</li>
                <li>Extended hours</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Venue Enquiry</a>
                <a href="tel:+6569569898" class="action-button">📞 Call for Special Arrangements</a>
            </div>
        </div>"""

    def _ces_info_response(self):
        return """<div class="response-box">
            <h3>ℹ️ About Changi Experience Studio</h3>
            
            <p>Changi Experience Studio is an immersive digital attraction located at Jewel Changi Airport:</p>
            
            <p><strong>Key Features:</strong></p>
            <ul>
                <li>Over 20 interactive digital installations</li>
                <li>Cutting-edge projection mapping technology</li>
                <li>Multi-sensory experiences</li>
                <li>Interactive games and challenges</li>
            </ul>
            
            <p><strong>Highlights:</strong></p>
            <ul>
                <li>Virtual airport control tower experience</li>
                <li>Interactive timeline of Changi's history</li>
                <li>Future airport concept showcase</li>
                <li>Multi-player aviation challenges</li>
            </ul>
            
            <p><strong>Recommended Duration:</strong> 1.5-2 hours</p>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/attractions/ces.html" class="action-button">🌐 Official Website</a>
                <a href="https://tickets.jewelchangiairport.com/" class="action-button">🎟️ Buy Tickets</a>
            </div>
        </div>"""

    def _ces_facilities_response(self):
        return """<div class="response-box">
            <h3>🏢 Changi Experience Studio Facilities</h3>
            
            <p><strong>Accessibility:</strong></p>
            <ul>
                <li>Wheelchair accessible</li>
                <li>Elevator access to all areas</li>
                <li>Accessible restrooms</li>
            </ul>
            
            <p><strong>Amenities:</strong></p>
            <ul>
                <li>Lockers available (SGD 2 per use)</li>
                <li>Free WiFi throughout</li>
                <li>Charging stations</li>
                <li>Rest area with seating</li>
            </ul>
            
            <p><strong>Services:</strong></p>
            <ul>
                <li>Multilingual staff (English, Mandarin, Malay, Tamil)</li>
                <li>First aid available</li>
                <li>Lost & found service</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/plan-your-visit/accessibility.html" class="action-button">♿ Accessibility Info</a>
                <a href="tel:+6569569898" class="action-button">📞 Contact for Special Needs</a>
            </div>
        </div>"""

    def _ces_activities_response(self):
        return """<div class="response-box">
            <h3>🎮 Changi Experience Studio Activities</h3>
            
            <p><strong>Interactive Zones:</strong></p>
            <ul>
                <li><strong>Story of Changi</strong> - Immersive digital timeline</li>
                <li><strong>Control Tower Challenge</strong> - Virtual air traffic control</li>
                <li><strong>Future Airport</strong> - Design your dream airport</li>
                <li><strong>Amazing Runway</strong> - Multi-player racing game</li>
            </ul>
            
            <p><strong>Special Experiences:</strong></p>
            <ul>
                <li><strong>Virtual Skydiving</strong> - 4D wind tunnel experience</li>
                <li><strong>Holographic Displays</strong> - Interactive 3D projections</li>
                <li><strong>Sound Garden</strong> - Create music with motion</li>
            </ul>
            
            <p><strong>Daily Schedule:</strong></p>
            <ul>
                <li>Main exhibits: Open all day</li>
                <li>Special shows: 12PM, 3PM, 6PM (weekends only)</li>
                <li>Guided tours: 11AM & 4PM (advance booking required)</li>
            </ul>
            
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en/attractions/ces.html" class="action-button">🌐 Activity Details</a>
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Book Guided Tour</a>
            </div>
        </div>"""

    def _thank_you_response(self):
        return """<div class="response-box">
            <h3>You're welcome! ✨</h3>
            <p>Is there anything else I can help you with today?</p>
            <div class="quick-options">
                <button class="quick-btn" onclick="askQuestion('opening hours')">⏰ Hours</button>
                <button class="quick-btn" onclick="askQuestion('ticket prices')">🎟️ Tickets</button>
                <button class="quick-btn" onclick="askQuestion('attractions')">🏆 Attractions</button>
                <button class="quick-btn" onclick="askQuestion('learning journey')">🎓 Learning Journey</button>
            </div>
        </div>"""

    def _unknown_question_response(self):
        return """<div class="response-box">
            <h3>🤔 Special Request</h3>
            <p>I couldn't find an answer to your specific question, but our staff would be happy to help!</p>
            <p>Please fill out our enquiry form and we'll get back to you within 2 working days.</p>
            
            <div class="action-buttons">
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Enquiry Form</a>
                <a href="tel:+6569569898" class="action-button">📞 Call +65 6956 9898</a>
            </div>
            
            <p>In the meantime, you might find these options helpful:</p>
            <div class="quick-options">
                <button class="quick-btn" onclick="askQuestion('opening hours')">⏰ Hours</button>
                <button class="quick-btn" onclick="askQuestion('ticket prices')">🎟️ Tickets</button>
                <button class="quick-btn" onclick="askQuestion('contact')">📞 Contact</button>
            </div>
        </div>"""

    def _default_response(self):
        return """<div class="response-box">
            <h3>🤔 Need More Help?</h3>
            <p>Try asking about:</p>
            <div class="quick-options">
                <button class="quick-btn" onclick="askQuestion('opening hours')">⏰ Hours</button>
                <button class="quick-btn" onclick="askQuestion('ticket prices')">🎟️ Tickets</button>
                <button class="quick-btn" onclick="askQuestion('singapore deal')">🇸🇬 SG60 Deal</button>
                <button class="quick-btn" onclick="askQuestion('contact')">📞 Contact</button>
                <button class="quick-btn" onclick="askQuestion('how to get there')">🚍 Directions</button>
                <button class="quick-btn" onclick="askQuestion('learning journey')">🎓 Learning Journey</button>
            </div>
            <div class="action-buttons">
                <a href="https://www.jewelchangiairport.com/en.html" class="action-button">🌐 Official Website</a>
                <a href="https://forms.office.com/r/xfXGFUDyQx" class="action-button">📝 Enquiry Form</a>
            </div>
        </div>"""

