document.addEventListener('DOMContentLoaded', function(event) {
    fetch('/blog/tiny/get-key/') // The path defined in urls
        .then(response => response.json())
        .then(data => {
            const tiny = data.tiny_key;
            // Checking if the key if fetched successfully before using it
            if (!tiny) {
                throw new Error('API key is not available');
            }
            // Constructing the Script element for TinyMCE
            let sc = document.createElement('script');
            sc.src = `https://cdn.tiny.cloud/1/${tiny}/tinymce/7/tinymce.min.js`;
            sc.referrerPolicy = 'origin';
            // Initializing it after Successful loading
            sc.onload = () => {
                tinymce.init({
                    selector: '#id_content',  // The Textarea element ID
                    width: 600,
                    height: 300,
                    plugins: [
                    'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
                    'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime',
                    'media', 'table', 'emoticons', 'help'
                    ],
                    toolbar: 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | ' +
                    'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
                    'forecolor backcolor emoticons | help',
                    menu: {
                    favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
                    },
                    menubar: 'favs file edit view insert format tools table help',
                    content_css: 'css/content.css'
                });
            }
            // Inserting in the Head Element
            document.head.appendChild(sc);

        })
        // Errors arising from fetching the Key
        .catch(error => {
            console.error('Error fetching the Tiny Key:', error);
        });
});
