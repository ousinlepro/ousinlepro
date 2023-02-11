
const submitButton = document.getElementById("submit-button");
const commandInput = document.getElementById("command-input");
const commentInput = document.getElementById("comment-input");
const commandList = document.getElementById("command-list");

let commands = [];

if (localStorage.getItem("commands")) {
  commands = JSON.parse(localStorage.getItem("commands"));
  commands.forEach(function(command, index) {
    const li = document.createElement("li");
    li.innerHTML = `<pre>${command.command}</pre><p>${command.comment}</p><button id="delete-${index}" class="delete-button">Supprimer</button>`;
    commandList.appendChild(li);

    const deleteButton = document.getElementById(`delete-${index}`);
    deleteButton.addEventListener("click", function() {
      commands.splice(index, 1);
      localStorage.setItem("commands", JSON.stringify(commands));
      li.remove();
    });
  });
}

submitButton.addEventListener("click", function() {
  const command = commandInput.value;
  const comment = commentInput.value;
  const li = document.createElement("li");
  const index = commands.length;
  li.innerHTML = `<pre>${command}</pre><p>${comment}</p><button id="delete-${index}" class="delete-button">Supprimer</button>`;
  commandList.appendChild(li);
  commands.push({ command: command, comment: comment });
  localStorage.setItem("commands", JSON.stringify(commands));

  const deleteButton = document.getElementById(`delete-${index}`);
  deleteButton.addEventListener("click", function() {
    commands.splice(index, 1);
    localStorage.setItem("commands", JSON.stringify(commands));
    li.remove();
  });
});