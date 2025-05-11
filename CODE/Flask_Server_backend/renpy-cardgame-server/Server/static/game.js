let playerName = prompt("Enter your player name:");

document.getElementById("joinBtn").addEventListener("click", async () => {
    const res = await fetch("/join", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({player: playerName})
    });
    const data = await res.json();
    updateHand(data.hand);
});

document.getElementById("playBtn").addEventListener("click", async () => {
    const res = await fetch("/play", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({player: playerName})
    });
    const data = await res.json();
    if (data.playedCard) {
        alert(`${playerName} played: ${data.playedCard} → ${data.result}`);
        updateHand(data.newHand);
        document.getElementById("score").textContent = "Score: " + data.score;
    } else {
        alert(data.message);
    }
});

function updateHand(hand) {
    document.getElementById("hand").textContent = "Your hand: " + hand.join(", ");
}
