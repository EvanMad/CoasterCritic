
function add_like(review_id) {

    let like_icon = document.getElementById(review_id + '-icon');
    let liked = like_icon.classList.contains('liked')

    const data = {
        review_id: review_id
    };

    let endpoint = "/"
    if(!liked)
    {
        endpoint = '/add_like';
    } else
    {
        endpoint = '/remove_like';
    }

    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Liked', data);
        likes_count = data.likes
        like_counter = document.getElementById(review_id + '-likes');
        like_counter.innerText = likes_count.toString();

        like_icon = document.getElementById(review_id + '-icon');
        like_icon.classList.toggle('liked');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}