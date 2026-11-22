site = {
    "Home": {
        "About": {},
        "Products": {
            "Electronics": {},
            "Books": {}
        },
        "Contact": {}
    }
}
def find_page(current, target, pages, path):   # pages is the dictionary containing the children of the current page
    path.append(current)
    if current == target:
        return True
    for page in pages:
        if find_page(page, target, pages[page], path):
            return True
    path.pop()                                      # backtracking
    return False
path = []
find_page("Home", "Books", site["Home"], path)
print("Path:", " -> ".join(path))