<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Happy Birthday💖</title>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

  <style>
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background: url('background.jpeg') no-repeat center center fixed;
      background-size: cover;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
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
      width: 100%;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    h1 {
      font-family: 'Pacifico', cursive;
      font-size: 2.6rem;
      color: #ff4d6d;
      margin-bottom: 10px;
    }
    h2 {
      font-size: 1.2rem;
      font-weight: 400;
      margin-bottom: 20px;
    }
    p {
      font-size: 1rem;
      line-height: 1.7;
      margin: 12px 0;
      color: #444;
    }
    .photo {
      width: 180px;
      height: 180px;
      border-radius: 50%;
      object-fit: cover;
      border: 6px solid #ffb3c1;
      margin: 20px auto;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .gallery {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 20px;
    }
    .gallery img {
      width: 100%;
      border-radius: 15px;
      object-fit: cover;
      box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    .emoji {
      font-size: 2.5rem;
      margin: 15px 0;
    }
    button {
      margin-top: 25px;
      padding: 12px 30px;
      border: none;
      border-radius: 30px;
      background: linear-gradient(135deg, #ff4d6d, #ff8fa3);
      color: white;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: 0.3s;
    }
    button:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    }
    .page { display: none; }
    .page.active { display: block; }

    audio { display: none; }

    /* Responsive */
    @media (max-width: 768px) {
      .card { padding: 30px 20px; }
      h1 { font-size: 2.1rem; }
      .photo { width: 150px; height: 150px; }
      button { width: 100%; }
    }
    @media (max-width: 480px) {
      h1 { font-size: 1.9rem; }
      p { font-size: 0.95rem; }
    }
  </style>
</head>
<body>

  <div class="card">

    <!-- PAGE 1 : HAPPY BIRTHDAY -->
    <div class="page active" id="page1">
      <h1>Happy Birthday 🎂</h1>
      <h2><strong>Ulan</strong> 💕</h2>

      <img src="foto.jpeg" alt="Foto" class="photo" />

      <div class="emoji">🎉🎈💖</div>

      <p>
        Semoga kamu suka kadonya, maaf aku cuma bisa ngasih itu. Walaupun sederhana, aku harap bisa punya arti dan jadi sesuatu yang berkesan buat kamu..
      </p>

      <button onclick="goPage(2)">Lanjut 💌</button>
    </div>

    <!-- PAGE 2 : KATA-KATA -->
    <div class="page" id="page2">
      <h1>For You 💖</h1>

      <p>
        Semoga di ulang tahun ini, setiap langkah yang kamu jalani dipenuhi kebahagiaan, cinta, dan keberkahan 🥳🎂✨ semoga semua impianmu perlahan menjadi nyata, dan semoga aku selalu bisa ada di sampingmu, menemani setiap tawa, cerita, dan perjalanan hidupmu 🤍🐻
      </p>

      <p>
        Terima kasih udah jadi bagian terindah dalam hidup aku 🥰💐🐣
      </p>

      <div class="emoji">💝✨🌈</div>

      <button onclick="goPage(3)">Lihat Foto 📸</button>
    </div>

    <!-- PAGE 3 : FOTO -->
    <div class="page" id="page3">
      <h1>Our Memories 📷</h1>

      <div class="gallery">
        <img src="foto1.jpeg" alt="Foto 1">
        <img src="foto2.jpeg" alt="Foto 2">
        <img src="foto3.jpeg" alt="Foto 3">
        <img src="foto4.jpeg" alt="Foto 4">
        <img src="foto5.jpeg" alt="Foto 5">
        <img src="foto6.jpeg" alt="Foto 6">
      </div>

      <div class="emoji">💞🎉</div>

      <button onclick="goPage(1)">Ulangi 🔁</button>
    </div>

    <!-- MUSIC -->
    <audio id="bgMusic" loop>
      <source src="musik.mp3" type="audio/mpeg">
    </audio>

  </div>

  <script>
    function goPage(page) {
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      document.getElementById('page' + page).classList.add('active');

      if (page > 1) {
        document.getElementById('bgMusic').play();
      }
    }
  </script>

</body>
</html>

