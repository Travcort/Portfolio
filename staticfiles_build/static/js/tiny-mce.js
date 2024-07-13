document.addEventListener('DOMContentLoaded', function(event) {
    let sc = document.createElement('script');
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/i2y4463dnfp0anuuftpd29sqdcf3uskdqm163z33vpjahozx/tinymce/7/tinymce.min.js');
    sc.setAttribute('referrerpolicy', 'origin');

    sc.onload = () => {
        tinymce.init({
            selector: '#id_content',  // change this value according to your HTML
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

    document.head.appendChild(sc);
})