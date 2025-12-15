<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Happy Birthday My Love 💖</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
      background-size: 400% 400%;
      animation: gradient 10s ease infinite;
      color: #333;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      text-align: center;
    }
    @keyframes gradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    .card {
      background: rgba(255,255,255,0.95);
      padding: 40px 30px;
      border-radius: 25px;
      max-width: 520px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    h1 {
      font-size: 2.4rem;
      margin-bottom: 5px;
      color: #ff4d6d;
    }
    h2 {
      font-size: 1.2rem;
      margin-bottom: 20px;
      font-weight: normal;
    }
    .photo {
      width: 200px;
      height: 200px;
      border-radius: 50%;
      object-fit: cover;
      border: 6px solid #ffb3c1;
      margin: 20px auto;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    p {
      font-size: 1rem;
      line-height: 1.7;
      margin: 12px 0;
    }
    .emoji {
      font-size: 2.5rem;
      margin: 15px 0;
    }
    button {
      margin-top: 25px;
      padding: 12px 28px;
      border: none;
      border-radius: 30px;
      background: linear-gradient(135deg, #ff4d6d, #ff8fa3);
      color: white;
      font-size: 1rem;
      cursor: pointer;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    button:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    }
    footer {
      margin-top: 25px;
      font-size: 0.8rem;
      color: #777;
    }
    audio {
      margin-top: 20px;
      width: 100%;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Happy Birthday 🎂</h1>
    <h2>My Love, <strong>[Nama]</strong> 💕</h2>

    <!-- Ganti src dengan foto kamu -->
    <img src="foto.jpg" alt="Foto Ulang Tahun" class="photo" />

    <div class="emoji">🎉🎈💖🎁</div>

    <p>
      Di hari spesialmu ini, aku ingin kamu tahu betapa berharganya kamu
      dalam hidupku. Terima kasih sudah hadir, menemani, dan mengisi hari-hariku
      dengan cinta.
    </p>

    <p>
      Semoga setiap langkahmu dipenuhi kebahagiaan, tawa, dan mimpi-mimpi indah
      yang perlahan menjadi nyata. Aku selalu mendoakan yang terbaik untukmu.
    </p>

    <button onclick="showMessage()">Pesan Cinta 💌</button>

    <!-- Musik ulang tahun / romantis -->
    <!-- Ganti musik.mp3 dengan file musik kamu -->
    <audio controls autoplay loop>
      <source src="musik.mp3" type="audio/mpeg">
      Browser kamu tidak mendukung audio.
    </audio>

    <footer>
      <p>Dibuat dengan penuh cinta ❤️</p>
    </footer>
  </div>

  <script>
    function showMessage() {
      alert('💖 Selamat ulang tahun, sayang. Semoga kita selalu bersama dan bahagia 💖');
    }
  </script>
</body>
</html>
