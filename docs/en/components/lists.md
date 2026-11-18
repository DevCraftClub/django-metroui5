# Lists

MetroUI5 Django provides a comprehensive list component system for displaying structured data, navigation items, and organized content in various list formats.

## Basic Usage

```python
from metroui5.components import render_list

# Simple list
items = ["Item 1", "Item 2", "Item 3"]
list_html = render_list(items)
```

## Parameters

### `render_list(items, list_type="ul", **attrs)`

- **items** (list): List of items to display
- **list_type** (str): Type of list ("ul" for unordered, "ol" for ordered)
- **attrs** (dict): Additional HTML attributes

## Examples

### Basic List

```python
from metroui5.components import render_list

# Unordered list
items = ["Apple", "Banana", "Orange", "Grape"]
list_html = render_list(items)

# Ordered list
ordered_list = render_list(items, list_type="ol")
```

### List with Custom Classes

```python
list_html = render_list(
    items=["Home", "About", "Contact", "Services"],
    list_type="ul",
    class="list list-horizontal",
    id="main-navigation"
)
```

### List with Complex Items

```python
complex_items = [
    {"text": "Dashboard", "icon": "dashboard", "url": "/dashboard/"},
    {"text": "Users", "icon": "users", "url": "/users/"},
    {"text": "Settings", "icon": "cog", "url": "/settings/"},
    {"text": "Reports", "icon": "chart", "url": "/reports/"}
]

list_html = render_list(complex_items, class="list list-navigation")
```

## MetroUI List Classes

MetroUI5 provides several CSS classes for list styling:

### Style Classes

- `list` - Base list class
- `list-primary` - Primary list style
- `list-secondary` - Secondary list style
- `list-success` - Success list style
- `list-warning` - Warning list style
- `list-danger` - Danger list style
- `list-info` - Info list style

### Layout Classes

- `list-horizontal` - Horizontal list
- `list-vertical` - Vertical list (default)
- `list-inline` - Inline list
- `list-grid` - Grid-based list

### Size Classes

- `list-small` - Small list
- `list-large` - Large list
- `list-compact` - Compact list

### Interactive Classes

- `list-hover` - Hover effects
- `list-selectable` - Selectable items
- `list-sortable` - Sortable items
- `list-draggable` - Draggable items

## List Types

### Navigation List

```python
def create_navigation_list(menu_items):
    """Create navigation list with icons and links."""

    items = []
    for item in menu_items:
        item_html = f"""
        <a href="{item['url']}" class="list-item">
            <span class="mif-{item['icon']}"></span>
            <span class="list-item-text">{item['text']}</span>
        </a>
        """
        items.append(item_html)

    return render_list(items, class="list list-navigation")

# Usage
menu_items = [
    {"text": "Dashboard", "icon": "dashboard", "url": "/dashboard/"},
    {"text": "Users", "icon": "users", "url": "/users/"},
    {"text": "Products", "icon": "box", "url": "/products/"},
    {"text": "Orders", "icon": "cart", "url": "/orders/"},
    {"text": "Settings", "icon": "cog", "url": "/settings/"}
]

nav_list = create_navigation_list(menu_items)
```

### User List

```python
def create_user_list(users):
    """Create user list with avatars and information."""

    items = []
    for user in users:
        status_class = "success" if user['active'] else "default"
        item_html = f"""
        <div class="list-item user-item">
            <div class="user-avatar">
                <img src="{user.get('avatar', '/static/default-avatar.png')}" alt="Avatar">
            </div>
            <div class="user-info">
                <div class="user-name">{user['name']}</div>
                <div class="user-email">{user['email']}</div>
            </div>
            <div class="user-status">
                <span class="badge badge-{status_class}">
                    {'Active' if user['active'] else 'Inactive'}
                </span>
            </div>
        </div>
        """
        items.append(item_html)

    return render_list(items, class="list list-users")

# Usage
users = [
    {"name": "John Doe", "email": "john@example.com", "active": True, "avatar": "/static/avatars/john.jpg"},
    {"name": "Jane Smith", "email": "jane@example.com", "active": True, "avatar": "/static/avatars/jane.jpg"},
    {"name": "Bob Johnson", "email": "bob@example.com", "active": False, "avatar": "/static/avatars/bob.jpg"}
]

user_list = create_user_list(users)
```

### Task List

```python
def create_task_list(tasks):
    """Create task list with checkboxes and priorities."""

    items = []
    for task in tasks:
        priority_class = task.get('priority', 'normal')
        completed_class = "completed" if task.get('completed', False) else ""

        item_html = f"""
        <div class="list-item task-item {completed_class}">
            <div class="task-checkbox">
                <label class="checkbox">
                    <input type="checkbox" {'checked' if task.get('completed', False) else ''} data-role="checkbox">
                    <span class="check"></span>
                </label>
            </div>
            <div class="task-content">
                <div class="task-title">{task['title']}</div>
                <div class="task-description">{task.get('description', '')}</div>
            </div>
            <div class="task-meta">
                <span class="task-priority badge badge-{priority_class}">{priority_class.title()}</span>
                <span class="task-date">{task.get('due_date', '')}</span>
            </div>
        </div>
        """
        items.append(item_html)

    return render_list(items, class="list list-tasks")

# Usage
tasks = [
    {
        "title": "Complete project proposal",
        "description": "Write and submit the project proposal document",
        "priority": "high",
        "completed": False,
        "due_date": "2024-01-20"
    },
    {
        "title": "Review code changes",
        "description": "Review and approve pending code changes",
        "priority": "medium",
        "completed": True,
        "due_date": "2024-01-18"
    },
    {
        "title": "Update documentation",
        "description": "Update API documentation with new endpoints",
        "priority": "low",
        "completed": False,
        "due_date": "2024-01-25"
    }
]

task_list = create_task_list(tasks)
```

### File List

```python
def create_file_list(files):
    """Create file list with icons and metadata."""

    items = []
    for file in files:
        file_type = file.get('type', 'file')
        size_mb = file.get('size', 0) / (1024 * 1024)

        item_html = f"""
        <div class="list-item file-item">
            <div class="file-icon">
                <span class="mif-{file_type}"></span>
            </div>
            <div class="file-info">
                <div class="file-name">{file['name']}</div>
                <div class="file-meta">
                    {size_mb:.1f} MB • Modified {file.get('modified', 'Unknown')}
                </div>
            </div>
            <div class="file-actions">
                <button class="button button-mini" onclick="downloadFile('{file['id']}')">
                    <span class="mif-download"></span>
                </button>
                <button class="button button-mini" onclick="deleteFile('{file['id']}')">
                    <span class="mif-delete"></span>
                </button>
            </div>
        </div>
        """
        items.append(item_html)

    return render_list(items, class="list list-files")

# Usage
files = [
    {"id": 1, "name": "project-proposal.pdf", "type": "file-pdf", "size": 2048000, "modified": "2 days ago"},
    {"id": 2, "name": "presentation.pptx", "type": "file-powerpoint", "size": 5120000, "modified": "1 week ago"},
    {"id": 3, "name": "data-analysis.xlsx", "type": "file-excel", "size": 1024000, "modified": "3 days ago"},
    {"id": 4, "name": "team-photo.jpg", "type": "image", "size": 3072000, "modified": "1 day ago"}
]

file_list = create_file_list(files)
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_list items=list_items class="list list-primary"
%}
```

## Advanced Examples

### Sortable List

```python
def create_sortable_list(items, sortable=True):
    """Create sortable list with drag and drop functionality."""

    list_class = "list list-sortable" if sortable else "list"

    items_html = []
    for item in items:
        item_html = f"""
        <div class="list-item sortable-item" data-id="{item['id']}">
            <div class="sort-handle">
                <span class="mif-menu"></span>
            </div>
            <div class="item-content">
                {item['content']}
            </div>
        </div>
        """
        items_html.append(item_html)

    return render_list(items_html, class=list_class)

# Usage
sortable_items = [
    {"id": 1, "content": "First item"},
    {"id": 2, "content": "Second item"},
    {"id": 3, "content": "Third item"},
    {"id": 4, "content": "Fourth item"}
]

sortable_list = create_sortable_list(sortable_items)
```

### Filterable List

```python
def create_filterable_list(items, filter_options=None):
    """Create list with filtering capabilities."""

    if filter_options is None:
        filter_options = ["All", "Active", "Inactive", "Pending"]

    filter_html = """
    <div class="list-filters">
        <div class="filter-group">
            <label>Filter by status:</label>
            <select class="select" data-role="select" onchange="filterList(this.value)">
    """

    for option in filter_options:
        filter_html += f'<option value="{option.lower()}">{option}</option>'

    filter_html += """
            </select>
        </div>
        <div class="search-group">
            <input type="text" class="input" placeholder="Search items..." onkeyup="searchList(this.value)">
        </div>
    </div>
    """

    items_html = []
    for item in items:
        item_html = f"""
        <div class="list-item filterable-item" data-status="{item.get('status', 'all')}" data-search="{item['name'].lower()}">
            <div class="item-content">
                <div class="item-name">{item['name']}</div>
                <div class="item-description">{item.get('description', '')}</div>
            </div>
            <div class="item-status">
                <span class="badge badge-{item.get('status', 'default')}">{item.get('status', 'Unknown').title()}</span>
            </div>
        </div>
        """
        items_html.append(item_html)

    list_html = render_list(items_html, class="list list-filterable")

    return filter_html + list_html

# Usage
filterable_items = [
    {"name": "Project Alpha", "description": "Main project", "status": "active"},
    {"name": "Project Beta", "description": "Secondary project", "status": "pending"},
    {"name": "Project Gamma", "description": "Research project", "status": "inactive"},
    {"name": "Project Delta", "description": "New project", "status": "active"}
]

filterable_list = create_filterable_list(filterable_items)
```

### Paginated List

```python
def create_paginated_list(items, page_size=10, current_page=1):
    """Create list with pagination."""

    start_index = (current_page - 1) * page_size
    end_index = start_index + page_size
    page_items = items[start_index:end_index]

    # Create list items
    items_html = []
    for item in page_items:
        item_html = f"""
        <div class="list-item">
            <div class="item-content">
                <div class="item-title">{item['title']}</div>
                <div class="item-description">{item.get('description', '')}</div>
            </div>
        </div>
        """
        items_html.append(item_html)

    list_html = render_list(items_html, class="list list-paginated")

    # Create pagination
    total_pages = (len(items) + page_size - 1) // page_size
    pagination_html = f"""
    <div class="pagination">
        <button class="button" {'disabled' if current_page == 1 else ''} onclick="goToPage({current_page - 1})">
            Previous
        </button>
        <span class="page-info">Page {current_page} of {total_pages}</span>
        <button class="button" {'disabled' if current_page == total_pages else ''} onclick="goToPage({current_page + 1})">
            Next
        </button>
    </div>
    """

    return list_html + pagination_html

# Usage
paginated_items = [
    {"title": f"Item {i}", "description": f"Description for item {i}"}
    for i in range(1, 51)  # 50 items
]

paginated_list = create_paginated_list(paginated_items, page_size=10, current_page=1)
```

### List with Actions

```python
def create_action_list(items, actions=None):
    """Create list with action buttons for each item."""

    if actions is None:
        actions = [
            {"text": "Edit", "class": "button-primary", "onclick": "editItem"},
            {"text": "Delete", "class": "button-danger", "onclick": "deleteItem"}
        ]

    items_html = []
    for item in items:
        action_buttons = ""
        for action in actions:
            action_buttons += f"""
            <button class="button button-mini {action['class']}"
                    onclick="{action['onclick']}({item['id']})">
                {action['text']}
            </button>
            """

        item_html = f"""
        <div class="list-item action-item">
            <div class="item-content">
                <div class="item-title">{item['title']}</div>
                <div class="item-description">{item.get('description', '')}</div>
            </div>
            <div class="item-actions">
                {action_buttons}
            </div>
        </div>
        """
        items_html.append(item_html)

    return render_list(items_html, class="list list-actions")

# Usage
action_items = [
    {"id": 1, "title": "User Profile", "description": "Manage user profile settings"},
    {"id": 2, "title": "Account Settings", "description": "Configure account preferences"},
    {"id": 3, "title": "Privacy Settings", "description": "Control privacy and security options"}
]

action_list = create_action_list(action_items)
```

## JavaScript Integration

### List Filtering

```javascript
// Filter list items
function filterList(filterValue) {
	const items = document.querySelectorAll(".filterable-item");

	items.forEach((item) => {
		const status = item.getAttribute("data-status");
		if (filterValue === "all" || status === filterValue) {
			item.style.display = "block";
		} else {
			item.style.display = "none";
		}
	});
}

// Search list items
function searchList(searchTerm) {
	const items = document.querySelectorAll(".filterable-item");

	items.forEach((item) => {
		const searchText = item.getAttribute("data-search");
		if (searchText.includes(searchTerm.toLowerCase())) {
			item.style.display = "block";
		} else {
			item.style.display = "none";
		}
	});
}
```

### List Sorting

```javascript
// Sort list items
function sortList(sortBy, direction = "asc") {
	const list = document.querySelector(".list-sortable");
	const items = Array.from(list.querySelectorAll(".sortable-item"));

	items.sort((a, b) => {
		const aValue = a.querySelector(`[data-sort="${sortBy}"]`).textContent;
		const bValue = b.querySelector(`[data-sort="${sortBy}"]`).textContent;

		if (direction === "asc") {
			return aValue.localeCompare(bValue);
		} else {
			return bValue.localeCompare(aValue);
		}
	});

	// Re-append sorted items
	items.forEach((item) => list.appendChild(item));
}
```

### List Selection

```javascript
// Handle list item selection
document.querySelectorAll(".list-selectable .list-item").forEach((item) => {
	item.addEventListener("click", function () {
		// Toggle selection
		this.classList.toggle("selected");

		// Update selection count
		const selectedItems = document.querySelectorAll(".list-item.selected");
		updateSelectionCount(selectedItems.length);
	});
});

function updateSelectionCount(count) {
	const counter = document.querySelector(".selection-counter");
	if (counter) {
		counter.textContent = `${count} item(s) selected`;
	}
}
```

### Drag and Drop

```javascript
// Initialize drag and drop for sortable lists
function initializeSortableList() {
	const sortableList = document.querySelector(".list-sortable");

	if (sortableList) {
		sortableList.addEventListener("dragstart", function (e) {
			e.target.classList.add("dragging");
		});

		sortableList.addEventListener("dragend", function (e) {
			e.target.classList.remove("dragging");
		});

		sortableList.addEventListener("dragover", function (e) {
			e.preventDefault();
			const dragging = document.querySelector(".dragging");
			const afterElement = getDragAfterElement(sortableList, e.clientY);

			if (afterElement == null) {
				sortableList.appendChild(dragging);
			} else {
				sortableList.insertBefore(dragging, afterElement);
			}
		});
	}
}

function getDragAfterElement(container, y) {
	const draggableElements = [
		...container.querySelectorAll(".sortable-item:not(.dragging)"),
	];

	return draggableElements.reduce(
		(closest, child) => {
			const box = child.getBoundingClientRect();
			const offset = y - box.top - box.height / 2;

			if (offset < 0 && offset > closest.offset) {
				return { offset: offset, element: child };
			} else {
				return closest;
			}
		},
		{ offset: Number.NEGATIVE_INFINITY }
	).element;
}
```

## Best Practices

1. **Use appropriate list types**: Choose ul/ol based on content structure
2. **Keep items consistent**: Use consistent styling and layout for list items
3. **Provide clear actions**: Make action buttons obvious and accessible
4. **Handle empty states**: Show appropriate messages when lists are empty
5. **Optimize for performance**: Use pagination or virtualization for large lists
6. **Make it accessible**: Ensure keyboard navigation and screen reader support
7. **Use consistent spacing**: Apply consistent margins and padding

## Related Components

- [Navigation](navigation.md) - For navigation lists
- [Tables](tables.md) - For tabular data display
- [Cards](cards.md) - For card-based content organization
- [Pagination](pagination.md) - For paginated list content


## metroui5_list

```python
render_list([{'text': 'One', 'href': '/one'}])
```

Empty or invalid: `render_list([{'text': 'One', 'href': '/one'}])` returns `<ul class="list" data-role="list"><li><a href="/one">One</a></li></ul>`. An empty call returns `<ul class="list" data-role="list"></ul>`.

```django
{% metroui5_list items %}
```
