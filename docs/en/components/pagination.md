# Pagination

MetroUI5 Django provides a comprehensive pagination component system for navigating through large datasets and content pages.

## Basic Usage

```python
from metroui5.components import render_pagination

# Simple pagination
pagination_html = render_pagination(current_page=1, total_pages=10)
```

## Parameters

### `render_pagination(current_page, total_pages, **attrs)`

- **current_page** (int): Current page number (1-based)
- **total_pages** (int): Total number of pages
- **attrs** (dict): Additional HTML attributes

## Examples

### Basic Pagination

```python
from metroui5.components import render_pagination

# Simple pagination
pagination = render_pagination(current_page=3, total_pages=10)
```

### Pagination with Custom Classes

```python
pagination = render_pagination(
    current_page=5,
    total_pages=20,
    class="pagination pagination-large",
    id="main-pagination"
)
```

### Pagination with Custom Attributes

```python
pagination = render_pagination(
    current_page=1,
    total_pages=15,
    data_role="pagination",
    data_ajax="true"
)
```

## MetroUI Pagination Classes

MetroUI5 provides several CSS classes for pagination styling:

### Style Classes

- `pagination` - Base pagination class
- `pagination-primary` - Primary pagination style
- `pagination-secondary` - Secondary pagination style
- `pagination-success` - Success pagination style
- `pagination-warning` - Warning pagination style
- `pagination-danger` - Danger pagination style
- `pagination-info` - Info pagination style

### Size Classes

- `pagination-small` - Small pagination
- `pagination-large` - Large pagination
- `pagination-mini` - Mini pagination

### Layout Classes

- `pagination-centered` - Centered pagination
- `pagination-right` - Right-aligned pagination
- `pagination-compact` - Compact pagination

## Pagination Types

### Basic Numeric Pagination

```python
def create_numeric_pagination(current_page, total_pages, show_ellipsis=True):
    """Create numeric pagination with page numbers."""

    return render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-numeric"
    )

# Usage
numeric_pagination = create_numeric_pagination(5, 20)
```

### Pagination with First/Last

```python
def create_full_pagination(current_page, total_pages):
    """Create pagination with first, previous, next, last buttons."""

    pagination_html = f"""
    <nav class="pagination pagination-full">
        <ul class="pagination-list">
            <li class="pagination-item">
                <a href="?page=1" class="pagination-link {'disabled' if current_page == 1 else ''}">
                    <span class="mif-first"></span>
                </a>
            </li>
            <li class="pagination-item">
                <a href="?page={current_page - 1}" class="pagination-link {'disabled' if current_page == 1 else ''}">
                    <span class="mif-left"></span>
                </a>
            </li>
    """

    # Add page numbers
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)

    for page in range(start_page, end_page + 1):
        active_class = "active" if page == current_page else ""
        pagination_html += f"""
            <li class="pagination-item">
                <a href="?page={page}" class="pagination-link {active_class}">{page}</a>
            </li>
        """

    pagination_html += f"""
            <li class="pagination-item">
                <a href="?page={current_page + 1}" class="pagination-link {'disabled' if current_page == total_pages else ''}">
                    <span class="mif-right"></span>
                </a>
            </li>
            <li class="pagination-item">
                <a href="?page={total_pages}" class="pagination-link {'disabled' if current_page == total_pages else ''}">
                    <span class="mif-last"></span>
                </a>
            </li>
        </ul>
    </nav>
    """

    return pagination_html

# Usage
full_pagination = create_full_pagination(5, 20)
```

### Pagination with Page Info

```python
def create_info_pagination(current_page, total_pages, total_items, items_per_page):
    """Create pagination with page information."""

    start_item = (current_page - 1) * items_per_page + 1
    end_item = min(current_page * items_per_page, total_items)

    info_html = f"""
    <div class="pagination-info">
        Showing {start_item} to {end_item} of {total_items} entries
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-info"
    )

    return info_html + pagination_html

# Usage
info_pagination = create_info_pagination(3, 10, 95, 10)
```

### Pagination with Page Size Selector

```python
def create_pagination_with_size(current_page, total_pages, current_size=10, size_options=None):
    """Create pagination with page size selector."""

    if size_options is None:
        size_options = [10, 25, 50, 100]

    size_selector = f"""
    <div class="pagination-size">
        <label>Show:</label>
        <select class="select" onchange="changePageSize(this.value)">
    """

    for size in size_options:
        selected = "selected" if size == current_size else ""
        size_selector += f'<option value="{size}" {selected}>{size}</option>'

    size_selector += """
        </select>
        <span>per page</span>
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-size"
    )

    return size_selector + pagination_html

# Usage
pagination_with_size = create_pagination_with_size(2, 8, 25, [10, 25, 50])
```

## Template Usage

```html
{% load metroui5 %} {% metroui5_pagination current_page=3 total_pages=10
class="pagination pagination-primary" %}
```

## Advanced Examples

### Pagination with AJAX

```python
def create_ajax_pagination(current_page, total_pages, ajax_url="/api/data/"):
    """Create pagination with AJAX loading."""

    pagination_html = f"""
    <nav class="pagination pagination-ajax" data-ajax-url="{ajax_url}">
        <ul class="pagination-list">
    """

    # Previous button
    if current_page > 1:
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="{current_page - 1}">
                    <span class="mif-left"></span>
                </a>
            </li>
        """

    # Page numbers
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)

    if start_page > 1:
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="1">1</a>
            </li>
        """
        if start_page > 2:
            pagination_html += '<li class="pagination-item"><span class="pagination-ellipsis">...</span></li>'

    for page in range(start_page, end_page + 1):
        active_class = "active" if page == current_page else ""
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link {active_class}" data-page="{page}">{page}</a>
            </li>
        """

    if end_page < total_pages:
        if end_page < total_pages - 1:
            pagination_html += '<li class="pagination-item"><span class="pagination-ellipsis">...</span></li>'
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="{total_pages}">{total_pages}</a>
            </li>
        """

    # Next button
    if current_page < total_pages:
        pagination_html += f"""
            <li class="pagination-item">
                <a href="#" class="pagination-link" data-page="{current_page + 1}">
                    <span class="mif-right"></span>
                </a>
            </li>
        """

    pagination_html += """
        </ul>
    </nav>
    """

    return pagination_html

# Usage
ajax_pagination = create_ajax_pagination(5, 20, "/api/users/")
```

### Pagination with Jump to Page

```python
def create_jump_pagination(current_page, total_pages):
    """Create pagination with jump to page input."""

    jump_input = f"""
    <div class="pagination-jump">
        <label>Go to page:</label>
        <input type="number" class="input input-mini"
               min="1" max="{total_pages}" value="{current_page}"
               onchange="jumpToPage(this.value)">
        <button class="button button-mini" onclick="jumpToPage()">Go</button>
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-jump"
    )

    return pagination_html + jump_input

# Usage
jump_pagination = create_jump_pagination(5, 20)
```

### Pagination with Results Summary

```python
def create_summary_pagination(current_page, total_pages, total_items, items_per_page, search_term=""):
    """Create pagination with detailed results summary."""

    start_item = (current_page - 1) * items_per_page + 1
    end_item = min(current_page * items_per_page, total_items)

    summary_html = f"""
    <div class="pagination-summary">
        <div class="summary-text">
            {f'Results for "{search_term}": ' if search_term else ''}
            Showing {start_item} to {end_item} of {total_items} entries
        </div>
        <div class="summary-pages">
            Page {current_page} of {total_pages}
        </div>
    </div>
    """

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-with-summary"
    )

    return summary_html + pagination_html

# Usage
summary_pagination = create_summary_pagination(
    current_page=3,
    total_pages=10,
    total_items=95,
    items_per_page=10,
    search_term="python"
)
```

### Pagination with Custom Styling

```python
def create_custom_pagination(current_page, total_pages, theme="primary"):
    """Create pagination with custom theme styling."""

    theme_classes = {
        "primary": "pagination-primary",
        "success": "pagination-success",
        "warning": "pagination-warning",
        "danger": "pagination-danger",
        "info": "pagination-info"
    }

    theme_class = theme_classes.get(theme, "pagination-primary")

    return render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class=f"pagination {theme_class} pagination-custom"
    )

# Usage
custom_pagination = create_custom_pagination(5, 20, "success")
```

### Pagination with Loading States

```python
def create_loading_pagination(current_page, total_pages, loading=False):
    """Create pagination with loading state."""

    loading_class = "pagination-loading" if loading else ""

    pagination_html = render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class=f"pagination {loading_class}"
    )

    if loading:
        loading_indicator = """
        <div class="pagination-loading-indicator">
            <span class="spinner"></span>
            Loading...
        </div>
        """
        return pagination_html + loading_indicator

    return pagination_html

# Usage
loading_pagination = create_loading_pagination(5, 20, loading=True)
```

### Responsive Pagination

```python
def create_responsive_pagination(current_page, total_pages):
    """Create responsive pagination that adapts to screen size."""

    return render_pagination(
        current_page=current_page,
        total_pages=total_pages,
        class="pagination pagination-responsive"
    )

# Usage
responsive_pagination = create_responsive_pagination(5, 20)
```

## JavaScript Integration

### AJAX Pagination

```javascript
// Handle AJAX pagination
document
	.querySelectorAll(".pagination-ajax .pagination-link")
	.forEach((link) => {
		link.addEventListener("click", function (e) {
			e.preventDefault();

			const page = this.getAttribute("data-page");
			const ajaxUrl =
				this.closest(".pagination-ajax").getAttribute("data-ajax-url");

			loadPageContent(page, ajaxUrl);
		});
	});

function loadPageContent(page, url) {
	// Show loading state
	showPaginationLoading();

	// Make AJAX request
	fetch(`${url}?page=${page}`)
		.then((response) => response.json())
		.then((data) => {
			// Update content
			updateContent(data.content);

			// Update pagination
			updatePagination(data.pagination);

			// Hide loading state
			hidePaginationLoading();
		})
		.catch((error) => {
			console.error("Error loading page:", error);
			hidePaginationLoading();
		});
}

function showPaginationLoading() {
	const pagination = document.querySelector(".pagination");
	pagination.classList.add("pagination-loading");
}

function hidePaginationLoading() {
	const pagination = document.querySelector(".pagination");
	pagination.classList.remove("pagination-loading");
}
```

### Jump to Page

```javascript
// Handle jump to page
function jumpToPage(page) {
	const pageNum = parseInt(page);
	const totalPages = parseInt(
		document.querySelector(".pagination").getAttribute("data-total-pages")
	);

	if (pageNum >= 1 && pageNum <= totalPages) {
		// Navigate to page
		window.location.href = `?page=${pageNum}`;
	} else {
		alert(`Please enter a page number between 1 and ${totalPages}`);
	}
}
```

### Page Size Change

```javascript
// Handle page size change
function changePageSize(newSize) {
	const currentUrl = new URL(window.location);
	currentUrl.searchParams.set("page_size", newSize);
	currentUrl.searchParams.set("page", "1"); // Reset to first page

	window.location.href = currentUrl.toString();
}
```

### Pagination Events

```javascript
// Handle pagination events
document.querySelectorAll(".pagination").forEach((pagination) => {
	pagination.addEventListener("pagination-change", function (event) {
		console.log("Page changed to:", event.detail.page);

		// Update URL without page reload
		const url = new URL(window.location);
		url.searchParams.set("page", event.detail.page);
		window.history.pushState({}, "", url);
	});
});

// Custom pagination change event
function triggerPaginationChange(page) {
	const pagination = document.querySelector(".pagination");
	const event = new CustomEvent("pagination-change", {
		detail: { page: page },
	});
	pagination.dispatchEvent(event);
}
```

### Pagination Keyboard Navigation

```javascript
// Handle keyboard navigation
document.addEventListener("keydown", function (e) {
	const pagination = document.querySelector(".pagination");
	if (!pagination) return;

	const currentPage = parseInt(pagination.getAttribute("data-current-page"));
	const totalPages = parseInt(pagination.getAttribute("data-total-pages"));

	switch (e.key) {
		case "ArrowLeft":
			if (currentPage > 1) {
				navigateToPage(currentPage - 1);
			}
			break;
		case "ArrowRight":
			if (currentPage < totalPages) {
				navigateToPage(currentPage + 1);
			}
			break;
		case "Home":
			navigateToPage(1);
			break;
		case "End":
			navigateToPage(totalPages);
			break;
	}
});

function navigateToPage(page) {
	const pagination = document.querySelector(".pagination");
	const link = pagination.querySelector(`[data-page="${page}"]`);
	if (link) {
		link.click();
	}
}
```

## Best Practices

1. **Use appropriate page sizes**: Choose page sizes that balance performance and usability
2. **Provide clear navigation**: Make it obvious how to navigate between pages
3. **Show current position**: Always indicate the current page clearly
4. **Handle edge cases**: Account for first page, last page, and empty results
5. **Use consistent styling**: Apply consistent pagination styles across your application
6. **Consider mobile users**: Ensure pagination works well on mobile devices
7. **Provide alternatives**: Consider infinite scroll or "load more" for some use cases

## Related Components

- [Tables](tables.md) - For paginated table data
- [Lists](lists.md) - For paginated list content
- [Navigation](navigation.md) - For navigation between pages
- [Cards](cards.md) - For paginated card layouts
