// Navigation
document.addEventListener('DOMContentLoaded', () => {
    // Section Navigation
    const navBtns = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.section');

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetSection = btn.getAttribute('data-section');

            // Update active button
            navBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Update active section
            sections.forEach(s => s.classList.remove('active'));
            document.getElementById(targetSection).classList.add('active');
        });
    });

    // Initialize Charts
    initializeCharts();
});

function initializeCharts() {
    // English Preference Chart
    const englishPrefCtx = document.getElementById('englishPreferenceChart');
    if (englishPrefCtx) {
        new Chart(englishPrefCtx, {
            type: 'bar',
            data: {
                labels: [
                    'Casino and Sports\nMade Easy',
                    'Watch & Play',
                    'Play & Watch',
                    'Game On',
                    'The Game is On',
                    'Play Made Easy'
                ],
                datasets: [{
                    label: 'Votes (out of 50)',
                    data: [20, 17, 10, 2, 1, 0],
                    backgroundColor: [
                        'rgba(37, 99, 235, 0.8)',
                        'rgba(139, 92, 246, 0.8)',
                        'rgba(16, 185, 129, 0.8)',
                        'rgba(245, 158, 11, 0.8)',
                        'rgba(239, 68, 68, 0.8)',
                        'rgba(148, 163, 184, 0.3)'
                    ],
                    borderColor: [
                        'rgb(37, 99, 235)',
                        'rgb(139, 92, 246)',
                        'rgb(16, 185, 129)',
                        'rgb(245, 158, 11)',
                        'rgb(239, 68, 68)',
                        'rgb(148, 163, 184)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const value = context.parsed.y;
                                const percentage = ((value / 50) * 100).toFixed(0);
                                return `${value}/50 votes (${percentage}%)`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 50,
                        ticks: {
                            stepSize: 10
                        },
                        title: {
                            display: true,
                            text: 'Number of Votes'
                        }
                    },
                    x: {
                        ticks: {
                            autoSkip: false,
                            maxRotation: 45,
                            minRotation: 45
                        }
                    }
                }
            }
        });
    }

    // English Trust Chart
    const englishTrustCtx = document.getElementById('englishTrustChart');
    if (englishTrustCtx) {
        new Chart(englishTrustCtx, {
            type: 'doughnut',
            data: {
                labels: [
                    'Casino and Sports Made Easy',
                    'The Game is On',
                    'Play & Watch'
                ],
                datasets: [{
                    data: [47, 2, 1],
                    backgroundColor: [
                        'rgba(37, 99, 235, 0.8)',
                        'rgba(245, 158, 11, 0.8)',
                        'rgba(16, 185, 129, 0.8)'
                    ],
                    borderColor: [
                        'rgb(37, 99, 235)',
                        'rgb(245, 158, 11)',
                        'rgb(16, 185, 129)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 20,
                            font: {
                                size: 12
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const value = context.parsed;
                                const percentage = ((value / 50) * 100).toFixed(0);
                                return `${context.label}: ${value}/50 (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    }

    // Danish Preference Chart
    const danishPrefCtx = document.getElementById('danishPreferenceChart');
    if (danishPrefCtx) {
        new Chart(danishPrefCtx, {
            type: 'bar',
            data: {
                labels: [
                    'Se og spil',
                    'Casino og sport\ngjort nemt',
                    'Spillet er i gang',
                    'Spil og se',
                    'Leg gjort nemt',
                    'Spil i gang'
                ],
                datasets: [{
                    label: 'Votes (out of 50)',
                    data: [22, 10, 10, 3, 3, 2],
                    backgroundColor: [
                        'rgba(37, 99, 235, 0.8)',
                        'rgba(139, 92, 246, 0.8)',
                        'rgba(16, 185, 129, 0.8)',
                        'rgba(245, 158, 11, 0.8)',
                        'rgba(239, 68, 68, 0.8)',
                        'rgba(148, 163, 184, 0.3)'
                    ],
                    borderColor: [
                        'rgb(37, 99, 235)',
                        'rgb(139, 92, 246)',
                        'rgb(16, 185, 129)',
                        'rgb(245, 158, 11)',
                        'rgb(239, 68, 68)',
                        'rgb(148, 163, 184)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const value = context.parsed.y;
                                const percentage = ((value / 50) * 100).toFixed(0);
                                return `${value}/50 votes (${percentage}%)`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 50,
                        ticks: {
                            stepSize: 10
                        },
                        title: {
                            display: true,
                            text: 'Number of Votes'
                        }
                    },
                    x: {
                        ticks: {
                            autoSkip: false,
                            maxRotation: 45,
                            minRotation: 45
                        }
                    }
                }
            }
        });
    }

    // Danish Trust Chart
    const danishTrustCtx = document.getElementById('danishTrustChart');
    if (danishTrustCtx) {
        new Chart(danishTrustCtx, {
            type: 'doughnut',
            data: {
                labels: [
                    'Casino og sport gjort nemt',
                    'Se og spil'
                ],
                datasets: [{
                    data: [40, 10],
                    backgroundColor: [
                        'rgba(37, 99, 235, 0.8)',
                        'rgba(139, 92, 246, 0.8)'
                    ],
                    borderColor: [
                        'rgb(37, 99, 235)',
                        'rgb(139, 92, 246)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 20,
                            font: {
                                size: 12
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const value = context.parsed;
                                const percentage = ((value / 50) * 100).toFixed(0);
                                return `${context.label}: ${value}/50 (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    }

    // Set fixed height for chart canvases
    const chartCanvases = document.querySelectorAll('.chart-container canvas');
    chartCanvases.forEach(canvas => {
        canvas.style.height = '400px';
    });
}

// Smooth scroll to sections
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
