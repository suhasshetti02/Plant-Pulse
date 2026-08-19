const apiKey = '62afcb1e4d7f4c72b684b4222a175886';
const url = `https://newsapi.org/v2/everything?q=agriculture&apiKey=${apiKey}`;

async function fetchNews() {
    const response = await fetch(url);
    const data = await response.json();
    const articles = data.articles;
    let output = '';

    articles.forEach(article => {
        output += `
            <div class="news-article">
                <img src="${article.urlToImage}" alt="${article.title}">
                <div class="news-content">
                    <h2>${article.title}</h2>
                    <p>${article.description}</p>
                    <a href="${article.url}" target="_blank" class="read-more-btn">Read more</a>
                </div>
            </div>
        `;
    });

    document.getElementById('news-articles').innerHTML = output;
}

fetchNews();
