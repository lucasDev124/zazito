from flask import Flask, make_response

app = Flask(__name__)

# Configuración de Acceso
CEO_EMAIL = "lucasdev@gmail.com"
CEO_PASS = "kakas123"

# TU CONTENIDO HTML INTEGRAL
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>ZaZaAutosecure | 3D Elite Suite</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Plus+Jakarta+Sans:wght@300;500;700&display=swap');
        
        :root {
            --primary: #ff4e00;
            --primary-glow: rgba(255, 78, 0, 0.6);
            --bg: #020202;
            --glass: rgba(20, 20, 20, 0.7);
            --glass-border: rgba(255, 255, 255, 0.1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; scroll-behavior: smooth; }
        body { background-color: var(--bg); color: #fff; font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; }

        #canvas-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; }

        nav {
            position: fixed; top: 20px; left: 50%; transform: translateX(-50%);
            width: 90%; max-width: 1000px; padding: 12px 30px;
            background: rgba(0, 0, 0, 0.8); backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border); border-radius: 50px;
            display: flex; justify-content: space-between; align-items: center; z-index: 1000;
        }
        .nav-links { display: flex; gap: 20px; list-style: none; }
        .nav-links a { text-decoration: none; color: #888; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; transition: 0.3s; }
        .nav-links a:hover { color: var(--primary); }

        .hero { text-align: center; perspective: 1000px; padding-top: 180px; padding-bottom: 100px; }
        .title-3d {
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(2rem, 8vw, 4.5rem);
            font-weight: 900;
            color: #fff;
            text-transform: uppercase;
            display: inline-block;
            position: relative;
            transform-style: preserve-3d;
            animation: float3d 4s ease-in-out infinite;
            text-shadow: 
                0 1px 0 #ccc, 0 2px 0 #c9c9c9, 0 3px 0 #bbb, 0 4px 0 #b9b9b9, 
                0 5px 0 #aaa, 0 6px 1px rgba(0,0,0,.1), 0 0 5px rgba(0,0,0,.1), 
                0 1px 3px rgba(0,0,0,.3), 0 3px 5px rgba(0,0,0,.2), 0 5px 10px rgba(0,0,0,.25), 
                0 10px 10px rgba(0,0,0,.2), 0 20px 20px rgba(0,0,0,.15),
                0 0 30px var(--primary-glow);
        }
        @keyframes float3d {
            0%, 100% { transform: rotateX(10deg) rotateY(-10deg) translateY(0); }
            50% { transform: rotateX(20deg) rotateY(10deg) translateY(-20px); }
        }

        section { padding: 80px 10%; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; }
        
        .card {
            background: var(--glass); border: 1px solid var(--glass-border);
            padding: 35px; border-radius: 25px; backdrop-filter: blur(10px);
            transition: 0.4s; position: relative;
        }
        .card:hover { transform: translateY(-10px); border-color: var(--primary); box-shadow: 0 15px 40px rgba(0,0,0,0.4); }
        .card h3 { font-family: 'Orbitron'; color: var(--primary); margin-bottom: 15px; font-size: 1.1rem; }
        .card p { color: #999; font-size: 0.9rem; line-height: 1.6; }

        .bot-section { background: linear-gradient(180deg, transparent, #080300, transparent); }
        .discord-btn {
            display: inline-block; margin-top: 20px; padding: 10px 25px;
            background: #5865F2; color: #fff; border-radius: 50px;
            text-decoration: none; font-weight: bold; transition: 0.3s;
        }
        .discord-btn:hover { transform: scale(1.1); box-shadow: 0 0 20px rgba(88, 101, 242, 0.4); }

        .staff-flex { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; margin-top: 40px; }
        .ceo-card { 
            background: var(--glass); padding: 25px; border-radius: 30px; 
            border: 1px solid var(--glass-border); text-align: center; width: 250px; 
        }
        .ceo-img { width: 100px; height: 100px; border-radius: 50%; border: 2px solid var(--primary); margin-bottom: 15px; }

        .reveal { opacity: 0; transform: translateY(30px); transition: 0.8s ease-out; }
        .reveal.active { opacity: 1; transform: translateY(0); }
    </style>
</head>
<body>
    <canvas id="canvas-bg"></canvas>
    <nav>
        <div style="font-family:'Orbitron'; color:var(--primary); font-size: 1.1rem; letter-spacing: 1px;">ZAZA SECURE</div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#bots">Discord Bots</a></li>
            <li><a href="#features">Comandos</a></li>
            <li><a href="#staff">Staff</a></li>
        </ul>
    </nav>
    <section id="home" class="hero">
        <h1 class="title-3d">ZAZAAUTOSECURE</h1>
        <p style="color: #666; font-size: 1.1rem; max-width: 600px; margin: 40px auto 0;">
            Elevando los estándares de seguridad y automatización en el ecosistema de Minecraft y Discord.
        </p>
    </section>
    <section id="bots" class="bot-section">
        <h2 style="font-family:'Orbitron'; text-align: center; margin-bottom: 40px; color: #fff;">DISCORD ECOSYSTEM</h2>
        <div class="grid">
            <div class="card reveal">
                <h3>ZaZa Manager</h3>
                <p>Contamos con Bots de Discord muy interesantes diseñados para la gestión masiva de licencias y el control de claims en tiempo real.</p>
            </div>
            <div class="card reveal">
                <h3>Ghost Sentry</h3>
                <p>Un bot especializado en la protección de servidores, detectando intrusiones y vinculaciones sospechosas antes de que ocurran.</p>
            </div>
            <div class="card reveal">
                <h3>Market Bot</h3>
                <p>Automatiza tus ventas y entregas de cuentas. Podréis encontrar más información detallada y manuales de uso en nuestro Discord oficial.</p>
                <a href="https://discord.gg/7Qd9ggYV" class="discord-btn"><i class="fab fa-discord"></i> UNIRSE AL DISCORD</a>
            </div>
        </div>
    </section>
    <section id="features">
        <h2 style="font-family:'Orbitron'; text-align: center; margin-bottom: 40px;">COMMANDS MANUAL</h2>
        <div class="grid">
            <div class="card reveal">
                <h3>/secure master</h3>
                <p>El comando definitivo. Cambia correos, deshabilita 2FA y genera códigos de recuperación en segundos.</p>
            </div>
            <div class="card reveal">
                <h3>/quarantine v2</h3>
                <p>Mantiene al usuario legítimo fuera de su propia cuenta mediante una saturación de paquetes en los servidores de autenticación.</p>
            </div>
            <div class="card reveal">
                <h3>Zyger Exploit</h3>
                <p>Acceso profundo a las credenciales de Windows vinculadas, permitiendo el bypass de seguridad biométrica.</p>
            </div>
        </div>
    </section>
    <section id="staff">
        <h2 style="font-family:'Orbitron'; text-align: center; margin-bottom: 40px;">THE CEOS</h2>
        <div class="staff-flex">
            <div class="ceo-card reveal">
                <img src="https://ui-avatars.com/api/?name=JX&background=ff4e00&color=000" class="ceo-img">
                <h4 style="font-family:'Orbitron'">jxan.ad</h4>
                <p style="color: var(--primary); font-size: 0.7rem;">LEAD DEVELOPER</p>
            </div>
            <div class="ceo-card reveal">
                <img src="https://ui-avatars.com/api/?name=G6&background=ff4e00&color=000" class="ceo-img">
                <h4 style="font-family:'Orbitron'">g6rn</h4>
                <p style="color: var(--primary); font-size: 0.7rem;">FOUNDER & CEO</p>
            </div>
        </div>
    </section>
    <script>
        const canvas = document.getElementById('canvas-bg');
        const ctx = canvas.getContext('2d');
        let particles = [];
        function init() {
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            for(let i=0; i<60; i++) particles.push({
                x: Math.random()*canvas.width, y: Math.random()*canvas.height,
                vx: (Math.random()-0.5)*0.3, vy: (Math.random()-0.5)*0.3,
                size: Math.random()*2
            });
        }
        function draw() {
            ctx.clearRect(0,0,canvas.width, canvas.height);
            ctx.fillStyle = "rgba(255, 78, 0, 0.4)";
            particles.forEach(p => {
                p.x += p.vx; p.y += p.vy;
                if(p.x<0 || p.x>canvas.width) p.vx *= -1;
                if(p.y<0 || p.y>canvas.height) p.vy *= -1;
                ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI*2); ctx.fill();
            });
            requestAnimationFrame(draw);
        }
        window.onresize = init;
        init(); draw();
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('active'); });
        }, { threshold: 0.1 });
        document.querySelectorAll('.reveal').forEach(r => observer.observe(r));
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return make_response(HTML_CONTENT)

# Handler para Vercel
def handler(request):
    return app(request)