const apiUrl = 'https://jsonplaceholder.typicode.com/posts';

// Data to be sent in the request body
const postData = {
  title: 'foo',
  body: 'bar',
  userId: 1,
};

// Configuring the Fetch API for a POST request
fetch(apiUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(postData),
})
  .then(response => {
    if (!response.ok) {
      throw new Error(`Network response was not ok: ${response.statusText}`);
    }
    return response.json();
  })
  .then(data => {
    console.log('Post response:', data);
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });
  function doPost(e) {
    // Data received from the client
    const receivedData = JSON.parse(e.postData.contents);
  
    // Perform any necessary processing with the received data
  
    // Return a response to the client
    return ContentService.createTextOutput('POST request received successfully');
  }
  