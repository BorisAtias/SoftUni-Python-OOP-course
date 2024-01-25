from math import ceil


class PhotoAlbum:
    PHOTO_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[]for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_count = ceil(photos_count / 4)
        return pages_count

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTO_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        separator = ["-" * 11]

        for page in self.photos:
            separator.append(' '.join("[]" for _ in range(len(page))))
            separator.append("-" * 11)

        return '\n'.join(separator)



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
