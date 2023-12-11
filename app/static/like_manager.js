
// Use AJAX to send like and unlike requests to the server and update the page dynamically
function add_like(event, review_id) {

    // Make sure that clicking like doesn't also open the review
    event.stopPropagation();

    // Handle whether this click event is adding or removing a like, and point the endpoint accordingly
    let like_icon = document.getElementById(review_id + '-icon');
    let liked = like_icon.classList.contains('liked')

    let endpoint = "/"
    if (!liked) {
        endpoint = '/add_like';
    } else {
        endpoint = '/remove_like';
    }

    // Package request payload
    const data = {
        review_id: review_id
    };

    // Setup request and send to endpoint
    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            // Handle server response
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Liked', data);
            // Update likes count on page
            likes_count = data.likes
            like_counter = document.getElementById(review_id + '-likes');
            like_counter.innerText = likes_count.toString();

            // Toggle whether the like button is filled in or not, indicated whether the user has liked the review
            like_icon = document.getElementById(review_id + '-icon');
            like_icon.classList.toggle('liked');
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
        });
}