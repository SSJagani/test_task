function showPdf(pdfUrl){
    const pull_button = document.getElementById('pull_button')

    const URL = pull_button.getAttribute('data-value')
    console.log(URL)
    var pdfViewer = document.getElementById('pdfViewer');
    pdfViewer.src = URL;
    // pdfViewer.src = 'static/admin/js/myapp.js';
    pdfViewer.style.display = 'block';
    return false;
}