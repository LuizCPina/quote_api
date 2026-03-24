/* main.js */

/* FRASERANDOM */
const quoteText = document.getElementById('quote-text');
const quoteAuthor = document.getElementById('quote-author');
const quoteCategory = document.getElementById('quote-category');

document.getElementById('new-quote-btn').addEventListener('click', () => {
    quoteText.textContent = 'Carregando...';
    quoteAuthor.textContent = '';
    quoteCategory.textContent = '';
    fetch('/quotes/random/')
        .then(res => res.json())
        .then(data => {
            quoteText.textContent = data.text;
            quoteAuthor.textContent = data.author ? `- ${data.author}` : '';
            quoteCategory.textContent = data.category ? `${data.category}` : '';
        })
        .catch(err => console.error('Erro ao buscar a frase:', err));
});

/* CRIAR NOVA FRASE */
const newQuoteText = document.getElementById('new-quote-text');
const newQuoteAuthor = document.getElementById('new-quote-author');
const newQuoteCategory = document.getElementById('new-quote-category');
const popup = document.getElementById('quote-success');

document.getElementById('add-quote-btn').addEventListener('click', () => {
    fetch('/quotes/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            text: newQuoteText.value,
            author: newQuoteAuthor.value,
            category: newQuoteCategory.value
        })
    })
    .then(res => {
        if (!res.ok) throw new Error('Erro ao criar frase');
        return res.json();
    })
    .then(data => {
        popup.showModal();
        newQuoteText.value = '';
        newQuoteAuthor.value = '';
        newQuoteCategory.value = '';
    })
    .catch(err => console.error(err));
});

document.getElementById('fechar-popup').addEventListener('click', () => {
    popup.close();
});