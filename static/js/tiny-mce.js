document.addEventListener('DOMContentLoaded', function(event) {
    let sc = document.createElement('script');
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/i2y4463dnfp0anuuftpd29sqdcf3uskdqm163z33vpjahozx/tinymce/7/tinymce.min.js');
    sc.setAttribute('referrerpolicy', 'origin');

    sc.onload = () => {
        tinymce.init({
            selector: '#id_content',  // change this value according to your HTML
            menubar: 'file edit view'
        });
    }

    document.head.appendChild(sc);
})