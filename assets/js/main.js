// === SCRIPT BLOCK 1 ===
window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };

// === SCRIPT BLOCK 2 ===
document.addEventListener('DOMContentLoaded', () => {
            // Barra de Progreso
            window.addEventListener('scroll', () => {
                const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
                const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                const scrolled = (winScroll / height) * 100;
                document.getElementById('scroll-progress').style.width = scrolled + "%";
            });

            // Animaciones de Revelado
            const reveals = document.querySelectorAll('.reveal');
            const revealOnScroll = () => {
                reveals.forEach(reveal => {
                    const windowHeight = window.innerHeight;
                    const elementTop = reveal.getBoundingClientRect().top;
                    if (elementTop < windowHeight - 150) reveal.classList.add('active');
                });
            };
            window.addEventListener('scroll', revealOnScroll);
            revealOnScroll();

            // Three.js Core - Optimizado para móvil
            const container = document.getElementById('canvas-container');
            const toggleBtnMobile = document.getElementById('toggle-demo-mobile');
            const toggleBtnDesktop = document.getElementById('toggle-demo-desktop');
            const statusText = document.getElementById('demo-status');
            const descTextMobile = document.getElementById('demo-desc');
            const descTextDesktop = document.getElementById('demo-desc-desktop');

            let scene, camera, renderer, particles, networkLines;
            let mouseX = 0, mouseY = 0;
            let isClarity = false;
            let transitionFactor = 0;

            // Reducir partículas en móvil para mejor rendimiento
            const isMobile = window.innerWidth < 768;
            const PARTICLE_COUNT = isMobile ? 1000 : 3000;
            const chaosPositions = new Float32Array(PARTICLE_COUNT * 3);
            const clarityPositions = new Float32Array(PARTICLE_COUNT * 3);
            const currentPositions = new Float32Array(PARTICLE_COUNT * 3);

            function createNodeTexture() {
                const canvas = document.createElement('canvas');
                canvas.width = isMobile ? 64 : 128;
                canvas.height = isMobile ? 64 : 128;
                const ctx = canvas.getContext('2d');
                const size = isMobile ? 32 : 64;
                const grad = ctx.createRadialGradient(size, size, 0, size, size, size);
                grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
                grad.addColorStop(0.3, 'rgba(255, 255, 255, 0.8)');
                grad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                ctx.fillStyle = grad;
                ctx.arc(size, size, size - 2, 0, Math.PI * 2);
                ctx.fill();
                return new THREE.CanvasTexture(canvas);
            }

            function updateUI() {
                const toggleText = isClarity ? "REINICIAR ESCANEO" : "TRANSFORMAR EN CLARIDAD";
                const statusTextContent = isClarity ? "ESTADO: CLARIDAD MAGISTRAL" : "ESTADO: CAOS URBANO";
                const statusColor = isClarity ? "#00FF5E" : "#FF0000";
                const descContent = isClarity ?
                    "Red nodal estabilizada. Estructura detectada." :
                    "Infoxicación detectada. El flujo está bloqueado por el ruido. Iniciar protocolo SRAP para estabilizar la red estructural.";

                statusText.innerText = statusTextContent;
                statusText.style.color = statusColor;

                if (descTextMobile) descTextMobile.innerText = descContent;
                if (descTextDesktop) descTextDesktop.innerText = descContent;

                if (toggleBtnMobile) toggleBtnMobile.innerText = toggleText;
                if (toggleBtnDesktop) toggleBtnDesktop.innerText = toggleText;

                particles.material.color.set(isClarity ? 0x00FF5E : 0xFF0000);
            }

            function init3D() {
                try {
                    scene = new THREE.Scene();
                    camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 1, 1000);
                    camera.position.z = 50;

                    renderer = new THREE.WebGLRenderer({
                        antialias: !isMobile,
                        alpha: true,
                        powerPreference: "high-performance"
                    });
                    renderer.setSize(container.clientWidth, container.clientHeight);
                    renderer.setPixelRatio(Math.min(window.devicePixelRatio, isMobile ? 1.5 : 2));
                    container.appendChild(renderer.domElement);

                    for(let i=0; i < PARTICLE_COUNT; i++) {
                        const i3 = i * 3;
                        chaosPositions[i3] = (Math.random() - 0.5) * 120;
                        chaosPositions[i3+1] = (Math.random() - 0.5) * 120;
                        chaosPositions[i3+2] = (Math.random() - 0.5) * 120;

                        const phi = Math.acos(-1 + (2 * i) / PARTICLE_COUNT);
                        const theta = Math.sqrt(PARTICLE_COUNT * Math.PI) * phi;
                        const r = 24;
                        clarityPositions[i3] = r * Math.cos(theta) * Math.sin(phi);
                        clarityPositions[i3+1] = r * Math.sin(theta) * Math.sin(phi);
                        clarityPositions[i3+2] = r * Math.cos(phi);

                        currentPositions[i3] = chaosPositions[i3];
                        currentPositions[i3+1] = chaosPositions[i3+1];
                        currentPositions[i3+2] = chaosPositions[i3+2];
                    }

                    const geo = new THREE.BufferGeometry();
                    geo.setAttribute('position', new THREE.BufferAttribute(currentPositions, 3));
                    particles = new THREE.Points(geo, new THREE.PointsMaterial({
                        size: isMobile ? 1.5 : 2.2,
                        map: createNodeTexture(),
                        transparent: true,
                        opacity: 1,
                        blending: THREE.AdditiveBlending,
                        depthWrite: false,
                        color: 0xFF0000
                    }));
                    scene.add(particles);

                    const lineIndices = [];
                    const lineStep = isMobile ? 40 : 25;
                    for(let i=0; i<PARTICLE_COUNT; i+=lineStep) {
                        for(let j=0; j<(isMobile ? 4 : 6); j++) {
                            lineIndices.push(i, (i + Math.floor(Math.random() * 60)) % PARTICLE_COUNT);
                        }
                    }
                    const lineGeo = new THREE.BufferGeometry();
                    lineGeo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(PARTICLE_COUNT * 3), 3));
                    lineGeo.setIndex(lineIndices);
                    networkLines = new THREE.LineSegments(lineGeo, new THREE.LineBasicMaterial({
                        color: 0x00FF5E,
                        transparent: true,
                        opacity: 0,
                        blending: THREE.AdditiveBlending
                    }));
                    scene.add(networkLines);

                    // Interacción táctil para móvil
                    if (isMobile) {
                        container.addEventListener('touchmove', (e) => {
                            e.preventDefault();
                            const rect = container.getBoundingClientRect();
                            const touch = e.touches[0];
                            mouseX = (touch.clientX - rect.left - rect.width/2) / 50;
                            mouseY = (touch.clientY - rect.top - rect.height/2) / 50;
                        }, { passive: false });
                    }

                    // Interacción con mouse para desktop
                    container.addEventListener('mousemove', (e) => {
                        const rect = container.getBoundingClientRect();
                        mouseX = (e.clientX - rect.left - rect.width/2) / 70;
                        mouseY = (e.clientY - rect.top - rect.height/2) / 70;
                    });

                    // Configurar botones (ambos funcionan igual)
                    const toggleButtons = [];
                    if (toggleBtnMobile) toggleButtons.push(toggleBtnMobile);
                    if (toggleBtnDesktop) toggleButtons.push(toggleBtnDesktop);

                    toggleButtons.forEach(btn => {
                        btn.addEventListener('click', () => {
                            isClarity = !isClarity;
                            updateUI();
                        });
                    });

                    let animationId;
                    const anim = () => {
                        const target = isClarity ? 1 : 0;
                        transitionFactor += (target - transitionFactor) * 0.05;
                        const pos = particles.geometry.attributes.position.array;
                        const lp = networkLines.geometry.attributes.position.array;
                        for(let i=0; i<PARTICLE_COUNT; i++) {
                            const i3 = i*3;
                            pos[i3] += ((chaosPositions[i3]*(1-transitionFactor) + clarityPositions[i3]*transitionFactor) - pos[i3]) * 0.08;
                            pos[i3+1] += ((chaosPositions[i3+1]*(1-transitionFactor) + clarityPositions[i3+1]*transitionFactor) - pos[i3+1]) * 0.08;
                            pos[i3+2] += ((chaosPositions[i3+2]*(1-transitionFactor) + clarityPositions[i3+2]*transitionFactor) - pos[i3+2]) * 0.08;
                            lp[i3] = pos[i3]; lp[i3+1] = pos[i3+1]; lp[i3+2] = pos[i3+2];
                        }
                        particles.geometry.attributes.position.needsUpdate = true;
                        networkLines.geometry.attributes.position.needsUpdate = true;
                        networkLines.material.opacity = transitionFactor * 0.35;
                        particles.rotation.y += 0.0025;
                        networkLines.rotation.y += 0.0025;
                        camera.position.x += (mouseX - camera.position.x) * 0.05;
                        camera.position.y += (-mouseY - camera.position.y) * 0.05;
                        camera.lookAt(scene.position);
                        renderer.render(scene, camera);
                        animationId = requestAnimationFrame(anim);
                    };

                    // ⚡ Bolt Optimization: Pause animation when off-screen to save resources
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting) {
                                if (!animationId) anim();
                            } else {
                                if (animationId) {
                                    cancelAnimationFrame(animationId);
                                    animationId = null;
                                }
                            }
                        });
                    }, { rootMargin: '200px' });
                    observer.observe(container);

                    // Redimensionar responsivo
                    window.addEventListener('resize', () => {
                        camera.aspect = container.clientWidth / container.clientHeight;
                        camera.updateProjectionMatrix();
                        renderer.setSize(container.clientWidth, container.clientHeight);
                    });

                } catch (e) {
                    console.error("Error al inicializar WebGL:", e);
                    container.innerHTML = '<div class="text-center text-white p-8"><p>La visualización 3D no está disponible en este dispositivo.</p></div>';
                }
            }
            init3D();
        });
