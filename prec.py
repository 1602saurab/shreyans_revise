
customer_actions = ["Entering the store", "Browsing books", "Seeking assistance from staff", "Making a purchase"]

frontstage_elements = ["Welcoming entrance", "Well-organized bookshelves", "Knowledgeable and friendly staff",
                      "Cozy reading corners", "Self-checkout stations", "Additional services (book recommendations, author signings)"]

backstage_processes = ["Inventory management", "Restocking shelves", "Staff coordination", "Book ordering processes",
                       "Cleaning and maintenance"]

support_processes = ["Staff training programs", "Efficient book ordering and delivery system", "Events planning for book launches and author signings"]

physical_evidence = ["Store layout conducive to easy navigation", "Clear signage for different sections",
                     "Creative displays to highlight featured books", "Comfortable seating areas", "Event posters and announcements"]

customer_touchpoints = {
    "Physical": ["Bookshelves", "Information desk", "Reading areas"],
    "Digital": ["Online book reservations", "Loyalty program app"]
}

service_providers = {
    "Bookstore staff": "Assisting customers, restocking shelves, providing recommendations",
    "Cashiers": "Processing purchases and payments",
    "Event coordinators": "Planning and executing events"
}

# Customer Experience
customer_experience = {
    "Pain Points": ["Long checkout lines", "Disorganized shelves"],
    "Improvements": ["Additional staff during peak hours", "Regular shelf organization"],
    "Opportunities": ["Loyalty programs", "Exclusive events"]
}


def print_section(title, elements):
    print(f"\n**{title}:**")
    for element in elements:
        print(f"   - {element}")

# Print  Data
print_section("Customer Actions", customer_actions)
print_section("Frontstage", frontstage_elements)
print_section("Backstage", backstage_processes)
print_section("Support Processes", support_processes)
print_section("Physical Evidence", physical_evidence)

# Customer Touchpoints
print_section("Customer Touchpoints", ["Physical Touchpoints:", *customer_touchpoints["Physical"], "Digital Touchpoints:", *customer_touchpoints["Digital"]])

# Service Providers
print_section("Service Providers", [f"- {provider}: {responsibilities}" for provider, responsibilities in service_providers.items()])

# Customer Experience
print_section("Customer Experience", ["Pain Points:", *customer_experience["Pain Points"],
                                     "Improvements:", *customer_experience["Improvements"],
                                     "Opportunities:", *customer_experience["Opportunities"]])
