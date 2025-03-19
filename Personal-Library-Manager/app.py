import streamlit as st
import json

# Setting page 
st.set_page_config(page_title="Library Manager", page_icon="📚")
st.title("📚 Personal Library Manager ")

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""
    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory. """
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        st.subheader("Add a New Book")
        book_title = st.text_input("Book Title")
        book_author = st.text_input("Author")
        publication_year = st.text_input("Publication Year")
        book_genre = st.text_input("Genre")
        is_book_read = st.checkbox("Have you read this book?")

        if st.button("Add Book"):
            new_book = {
                "title": book_title,
                "author": book_author,
                "year": publication_year,
                "genre": book_genre,
                "read": is_book_read,
            }
            self.book_list.append(new_book)
            self.save_to_file()
            st.success("Book added successfully!")

    def delete_book(self):
        """Remove a book from the collection using its title."""
        st.subheader("Remove a Book")
        book_title = st.text_input("Enter the title of the book to remove")

        if st.button("Delete Book"):
            for book in self.book_list:
                if book["title"].lower() == book_title.lower():
                    self.book_list.remove(book)
                    self.save_to_file()
                    st.success("Book removed successfully!")
                    return
            st.error("Book not found!")

    def find_book(self):
        """Search for books in the collection by title or author name."""
        st.subheader("Search for Books")
        search_type = st.radio("Search by:", ["Title", "Author"])
        search_text = st.text_input("Enter search term").lower()

        if st.button("Search"):
            found_books = [
                book
                for book in self.book_list
                if search_text in book["title"].lower()
                or search_text in book["author"].lower()
            ]
            if found_books:
                st.write("Matching Books:")
                for book in found_books:
                    reading_status = "Read" if book["read"] else "Unread"
                    st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
            else:
                st.warning("No matching books found.")

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        st.subheader("Update Book Details")
        book_title = st.text_input("Enter the title of the book you want to edit")

        if st.button("Find Book"):
            for book in self.book_list:
                if book["title"].lower() == book_title.lower():
                    st.write("Leave blank to keep existing value.")
                    book["title"] = st.text_input("New title", book["title"])
                    book["author"] = st.text_input("New author", book["author"])
                    book["year"] = st.text_input("New year", book["year"])
                    book["genre"] = st.text_input("New genre", book["genre"])
                    book["read"] = st.checkbox("Have you read this book?", book["read"])

                    if st.button("Save Changes"):
                        self.save_to_file()
                        st.success("Book updated successfully!")
                    return
            st.error("Book not found!")

    def show_all_books(self):
        """Display Books"""
        st.subheader("Your Book Collection")
        if not self.book_list:
            st.warning("Your collection is empty.")
            return

        for book in self.book_list:
            reading_status = "Read" if book["read"] else "Unread"
            st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        st.subheader("Reading Progress")
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        st.write(f"Total books in collection: {total_books}")
        st.write(f"Reading progress: {completion_rate:.2f}%")

    def run(self):
        """Run the main application"""
        menu = [
            "Add a New Book",
            "Remove a Book",
            "Search for Books",
            "Update Book Details",
            "View All Books",
            "View Reading Progress",
        ]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Add a New Book":
            self.create_new_book()
        elif choice == "Remove a Book":
            self.delete_book()
        elif choice == "Search for Books":
            self.find_book()
        elif choice == "Update Book Details":
            self.update_book()
        elif choice == "View All Books":
            self.show_all_books()
        elif choice == "View Reading Progress":
            self.show_reading_progress()

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.run()

# Footer
st.write("---")
# Adding some CSS for a centered and themed footer
st.markdown(
    """
    <div style="text-align: center; font-style: italic; color: #666;">
        <p>📚 "A reader lives a thousand lives before he dies." – George R.R. Martin 📚</p>
        <p>Created with ❤️ by Khawaja Abdul Moiz | Happy Reading! 📖✨</p>
    </div>
    """,
    unsafe_allow_html=True
)
