function createListElement(data) {
    let li = document.createElement("li");
    let album = document.createElement("div");
    album.classList.add("album");
    let title = document.createElement("div");
    title.classList.add("title");
    let artists = document.createElement("div");
    artists.classList.add("artists");

    let details = document.createElement("div");
    details.classList.add("details")

    album.innerText = `${data.album} (${data.year})`;
    title.innerText = `${data.original_name}`;
    artists.innerText = `${data.artists_name.join(", ")}`;

    details.appendChild(album);
    details.appendChild(title);
    details.appendChild(artists);
    li.appendChild(details);
    return li;
}

function createInfoIcon() {
    let icon = document.createElement("div");
    icon.classList.add("icon-for-details");
    let i = document.createElement("i");
    i.classList.add("fa");
    i.classList.add("fa-info");
    icon.appendChild(i);
    return icon;
}

function createTable(data) {
    let ul = document.getElementById("songs-list");
    ul.innerHTML = "";
    for (let i = data.length - 1; i >= 0; i--) {
        let li = createListElement(data[i]);
        li.appendChild(createInfoIcon());
        ul.appendChild(li);
    }
    document.getElementById("total-count").innerText = `Total: ${data.length}`;
}

function fetchSongs() {
  fetch('/data.json')
  .then((response) => response.json())
  .then((data) => createTable(data["data"]));
}

fetchSongs();