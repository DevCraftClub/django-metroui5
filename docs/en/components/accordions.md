# Accordions

MetroUI5 Django provides a flexible accordion component system for creating collapsible content sections that can be expanded and collapsed independently.

## Call

```python
from metroui5.components import render_accordion

render_accordion([{"title": "One", "content": "Text"}])
```

An empty list returns `<div class="accordion" id="accordion-component" data-role="accordion"></div>`. `None` raises `TypeError`.

In a template, pass the same list as `items`:

```django
{% metroui5_accordion items %}
```

## Basic Usage

```python
from metroui5.components import render_accordion

# Simple accordion
items = [
    {"title": "Section 1", "content": "Content for section 1"},
    {"title": "Section 2", "content": "Content for section 2"},
    {"title": "Section 3", "content": "Content for section 3"}
]

accordion_html = render_accordion(items)
```

## Parameters

### `render_accordion(items, **attrs)`

- **items** (list): List of accordion items, each containing:
  - `title` (str): Section title
  - `content` (str): Section content (can be HTML)
  - `active` (bool, optional): Whether this section is initially active
  - `disabled` (bool, optional): Whether this section is disabled
- **attrs** (dict): Additional HTML attributes for the accordion container

## Examples

### Basic Accordion

```python
from metroui5.components import render_accordion

items = [
    {"title": "What is MetroUI5?", "content": "MetroUI5 is a modern UI framework for creating responsive web applications."},
    {"title": "How do I install it?", "content": "You can install MetroUI5 via npm, CDN, or download the files directly."},
    {"title": "Is it free to use?", "content": "Yes, MetroUI5 is open source and free to use in your projects."}
]

accordion = render_accordion(items)
```

### Accordion with Active Section

```python
items = [
    {"title": "Getting Started", "content": "Getting started content...", "active": True},
    {"title": "Configuration", "content": "Configuration content..."},
    {"title": "Advanced Usage", "content": "Advanced usage content..."}
]

accordion = render_accordion(items, class="accordion accordion-primary")
```

### Accordion with Custom Classes

```python
accordion = render_accordion(
    items=[
        {"title": "Section 1", "content": "Content 1"},
        {"title": "Section 2", "content": "Content 2"},
        {"title": "Section 3", "content": "Content 3"}
    ],
    class="accordion accordion-large",
    id="main-accordion"
)
```

## MetroUI Accordion Classes

MetroUI5 provides several CSS classes for accordion styling:

### Style Classes

- `accordion` - Base accordion class
- `accordion-primary` - Primary accordion style
- `accordion-secondary` - Secondary accordion style
- `accordion-success` - Success accordion style
- `accordion-warning` - Warning accordion style
- `accordion-danger` - Danger accordion style
- `accordion-info` - Info accordion style

### Size Classes

- `accordion-small` - Small accordion
- `accordion-large` - Large accordion
- `accordion-compact` - Compact accordion

### Behavior Classes

- `accordion-multiple` - Allow multiple sections open
- `accordion-single` - Only one section open at a time
- `accordion-closeable` - Allow closing all sections

## Accordion Types

### FAQ Accordion

```python
def create_faq_accordion(faq_items):
    """Create FAQ accordion with common questions."""

    return render_accordion(
        faq_items,
        class="accordion accordion-faq"
    )

# Usage
faq_items = [
    {
        "title": "How do I get started with MetroUI5?",
        "content": "To get started, include the MetroUI5 CSS and JavaScript files in your project and begin using the components."
    },
    {
        "title": "Is MetroUI5 responsive?",
        "content": "Yes, MetroUI5 is fully responsive and works great on desktop, tablet, and mobile devices."
    },
    {
        "title": "Can I customize the theme?",
        "content": "Absolutely! MetroUI5 provides extensive theming options and CSS variables for customization."
    },
    {
        "title": "What browsers are supported?",
        "content": "MetroUI5 supports all modern browsers including Chrome, Firefox, Safari, and Edge."
    }
]

faq_accordion = create_faq_accordion(faq_items)
```

### Settings Accordion

```python
def create_settings_accordion(settings_groups):
    """Create settings accordion with grouped options."""

    items = []
    for group in settings_groups:
        content = "<form class='settings-form'>"
        for setting in group['settings']:
            if setting['type'] == 'checkbox':
                content += f"""
                <div class='form-group'>
                    <label class='checkbox'>
                        <input type='checkbox' data-role='checkbox' {'checked' if setting.get('value') else ''}>
                        <span class='check'></span>
                        {setting['label']}
                    </label>
                </div>
                """
            elif setting['type'] == 'select':
                content += f"""
                <div class='form-group'>
                    <label>{setting['label']}:</label>
                    <select class='select' data-role='select'>
                        {''.join([f'<option value="{opt["value"]}" {"selected" if opt["value"] == setting.get("value") else ""}>{opt["label"]}</option>' for opt in setting['options']])}
                    </select>
                </div>
                """
        content += "</form>"

        items.append({
            "title": group['title'],
            "content": content,
            "active": group.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-settings")

# Usage
settings_groups = [
    {
        "title": "General Settings",
        "active": True,
        "settings": [
            {"type": "checkbox", "label": "Enable notifications", "value": True},
            {"type": "select", "label": "Language", "value": "en", "options": [
                {"value": "en", "label": "English"},
                {"value": "es", "label": "Spanish"},
                {"value": "fr", "label": "French"}
            ]}
        ]
    },
    {
        "title": "Privacy Settings",
        "settings": [
            {"type": "checkbox", "label": "Allow data collection", "value": False},
            {"type": "checkbox", "label": "Share usage statistics", "value": True}
        ]
    }
]

settings_accordion = create_settings_accordion(settings_groups)
```

### Documentation Accordion

```python
def create_docs_accordion(doc_sections):
    """Create documentation accordion with code examples."""

    items = []
    for section in doc_sections:
        content = f"""
        <div class='doc-section'>
            <p>{section['description']}</p>
            <h4>Example:</h4>
            <pre><code>{section['code_example']}</code></pre>
            {f"<p><strong>Note:</strong> {section['note']}</p>" if section.get('note') else ""}
        </div>
        """

        items.append({
            "title": section['title'],
            "content": content,
            "active": section.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-docs")

# Usage
doc_sections = [
    {
        "title": "Basic Usage",
        "active": True,
        "description": "Learn how to create a basic accordion component.",
        "code_example": """from metroui5.components import render_accordion

items = [
    {"title": "Section 1", "content": "Content 1"},
    {"title": "Section 2", "content": "Content 2"}
]

accordion = render_accordion(items)""",
        "note": "Make sure to include the MetroUI5 CSS and JavaScript files."
    },
    {
        "title": "Advanced Configuration",
        "description": "Configure accordion behavior and styling.",
        "code_example": """accordion = render_accordion(
    items,
    class="accordion accordion-multiple",
    data_role="accordion"
)""",
        "note": "Use 'accordion-multiple' to allow multiple sections to be open."
    }
]

docs_accordion = create_docs_accordion(doc_sections)
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_accordion items=accordion_items class="accordion
accordion-primary" %}
```

## Advanced Examples

### Accordion with Icons

```python
def create_icon_accordion(items_with_icons):
    """Create accordion with icons in titles."""

    items = []
    for item in items_with_icons:
        title_with_icon = f"""
        <span class='accordion-title'>
            <span class='mif-{item['icon']}'></span>
            {item['title']}
        </span>
        """

        items.append({
            "title": title_with_icon,
            "content": item['content'],
            "active": item.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-with-icons")

# Usage
icon_items = [
    {"icon": "user", "title": "Profile", "content": "Manage your profile settings..."},
    {"icon": "cog", "title": "Settings", "content": "Configure application settings..."},
    {"icon": "shield", "title": "Security", "content": "Security and privacy options..."},
    {"icon": "bell", "title": "Notifications", "content": "Notification preferences..."}
]

icon_accordion = create_icon_accordion(icon_items)
```

### Accordion with Progress Indicators

```python
def create_progress_accordion(progress_items):
    """Create accordion showing progress through steps."""

    items = []
    for i, item in enumerate(progress_items):
        progress = item.get('progress', 0)
        status_class = "success" if progress == 100 else "warning" if progress > 0 else "default"

        title_with_progress = f"""
        <span class='accordion-title'>
            {item['title']}
            <span class='progress-indicator badge badge-{status_class}'>{progress}%</span>
        </span>
        """

        content = f"""
        <div class='step-content'>
            <p>{item['description']}</p>
            <div class='progress-bar'>
                <div class='progress-fill' style='width: {progress}%'></div>
            </div>
            {item['content']}
        </div>
        """

        items.append({
            "title": title_with_progress,
            "content": content,
            "active": item.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-progress")

# Usage
progress_items = [
    {
        "title": "Setup",
        "description": "Initial project setup",
        "progress": 100,
        "content": "Project setup completed successfully."
    },
    {
        "title": "Configuration",
        "description": "Configure application settings",
        "progress": 75,
        "content": "Most settings configured, some optional settings remaining."
    },
    {
        "title": "Testing",
        "description": "Run tests and validation",
        "progress": 25,
        "content": "Basic tests completed, comprehensive testing in progress."
    },
    {
        "title": "Deployment",
        "description": "Deploy to production",
        "progress": 0,
        "content": "Ready to begin deployment process."
    }
]

progress_accordion = create_progress_accordion(progress_items)
```

### Accordion with Form Validation

```python
def create_form_accordion(form_sections):
    """Create accordion with form sections and validation."""

    items = []
    for section in form_sections:
        content = f"""
        <form class='accordion-form' data-section='{section['id']}'>
            {section['form_content']}
            <div class='form-actions'>
                <button type='button' class='button button-primary' onclick='validateSection("{section['id']}")'>
                    Validate Section
                </button>
                <button type='button' class='button button-secondary' onclick='saveSection("{section['id']}")'>
                    Save Section
                </button>
            </div>
        </form>
        """

        items.append({
            "title": section['title'],
            "content": content,
            "active": section.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-form")

# Usage
form_sections = [
    {
        "id": "personal-info",
        "title": "Personal Information",
        "active": True,
        "form_content": """
        <div class='form-group'>
            <label>First Name:</label>
            <input type='text' class='input' name='first_name' required>
        </div>
        <div class='form-group'>
            <label>Last Name:</label>
            <input type='text' class='input' name='last_name' required>
        </div>
        <div class='form-group'>
            <label>Email:</label>
            <input type='email' class='input' name='email' required>
        </div>
        """
    },
    {
        "id": "contact-info",
        "title": "Contact Information",
        "form_content": """
        <div class='form-group'>
            <label>Phone:</label>
            <input type='tel' class='input' name='phone'>
        </div>
        <div class='form-group'>
            <label>Address:</label>
            <textarea class='textarea' name='address'></textarea>
        </div>
        """
    }
]

form_accordion = create_form_accordion(form_sections)
```

### Nested Accordion

```python
def create_nested_accordion(main_sections):
    """Create accordion with nested sub-sections."""

    items = []
    for section in main_sections:
        if section.get('subsections'):
            # Create nested accordion for subsections
            nested_items = []
            for subsection in section['subsections']:
                nested_items.append({
                    "title": subsection['title'],
                    "content": subsection['content']
                })

            nested_accordion = render_accordion(nested_items, class="accordion accordion-nested")
            content = f"""
            <div class='main-section'>
                <p>{section.get('description', '')}</p>
                {nested_accordion}
            </div>
            """
        else:
            content = section['content']

        items.append({
            "title": section['title'],
            "content": content,
            "active": section.get('active', False)
        })

    return render_accordion(items, class="accordion accordion-nested")

# Usage
nested_sections = [
    {
        "title": "Frontend Development",
        "description": "Frontend development technologies and tools.",
        "subsections": [
            {"title": "HTML/CSS", "content": "HTML5 and CSS3 fundamentals..."},
            {"title": "JavaScript", "content": "Modern JavaScript development..."},
            {"title": "Frameworks", "content": "React, Vue, Angular frameworks..."}
        ]
    },
    {
        "title": "Backend Development",
        "description": "Backend development technologies and tools.",
        "subsections": [
            {"title": "Python", "content": "Python web development..."},
            {"title": "Node.js", "content": "Node.js and Express..."},
            {"title": "Databases", "content": "SQL and NoSQL databases..."}
        ]
    }
]

nested_accordion = create_nested_accordion(nested_sections)
```

## JavaScript Integration

### Accordion Control

```javascript
// Programmatically open/close accordion sections
function toggleAccordionSection(accordionId, sectionIndex) {
	const accordion = document.querySelector(`#${accordionId}`);
	if (accordion) {
		const sections = accordion.querySelectorAll(".accordion-section");
		const section = sections[sectionIndex];
		if (section) {
			section.classList.toggle("active");
		}
	}
}

// Open all sections
function openAllSections(accordionId) {
	const accordion = document.querySelector(`#${accordionId}`);
	if (accordion) {
		const sections = accordion.querySelectorAll(".accordion-section");
		sections.forEach((section) => section.classList.add("active"));
	}
}

// Close all sections
function closeAllSections(accordionId) {
	const accordion = document.querySelector(`#${accordionId}`);
	if (accordion) {
		const sections = accordion.querySelectorAll(".accordion-section");
		sections.forEach((section) => section.classList.remove("active"));
	}
}
```

### Accordion Events

```javascript
// Handle accordion events
document.querySelectorAll(".accordion").forEach((accordion) => {
	accordion.addEventListener("accordion-open", function (event) {
		console.log("Accordion section opened:", event.detail.section);
	});

	accordion.addEventListener("accordion-close", function (event) {
		console.log("Accordion section closed:", event.detail.section);
	});

	accordion.addEventListener("accordion-toggle", function (event) {
		console.log("Accordion section toggled:", event.detail.section);
	});
});
```

### Accordion Validation

```javascript
// Validate accordion form sections
function validateAccordionSection(sectionId) {
	const section = document.querySelector(`[data-section="${sectionId}"]`);
	if (section) {
		const form = section.querySelector("form");
		const inputs = form.querySelectorAll(
			"input[required], select[required], textarea[required]"
		);

		let isValid = true;
		inputs.forEach((input) => {
			if (!input.value.trim()) {
				input.classList.add("input-error");
				isValid = false;
			} else {
				input.classList.remove("input-error");
			}
		});

		return isValid;
	}
	return false;
}

// Save accordion section
function saveSection(sectionId) {
	if (validateAccordionSection(sectionId)) {
		const form = document.querySelector(`[data-section="${sectionId}"] form`);
		const formData = new FormData(form);

		// Send data to server
		fetch("/save-section/", {
			method: "POST",
			body: formData,
		}).then((response) => {
			if (response.ok) {
				showNotification("Section saved successfully!", "success");
			} else {
				showNotification("Error saving section", "error");
			}
		});
	} else {
		showNotification("Please fill in all required fields", "warning");
	}
}
```

## Best Practices

1. **Use clear titles**: Make section titles descriptive and concise
2. **Organize logically**: Group related content in the same section
3. **Limit section count**: Don't create too many sections (5-7 max recommended)
4. **Provide visual feedback**: Use icons or indicators to show section status
5. **Handle loading states**: Show loading indicators for dynamic content
6. **Make it accessible**: Ensure keyboard navigation works properly
7. **Use consistent styling**: Apply consistent classes across your application

## Related Components

- [Panels](panels.md) - For collapsible content areas
- [Tabs](tabs.md) - For tabbed content organization
- [Cards](cards.md) - For card-based content organization
- [Forms](forms.md) - For form content in accordions
