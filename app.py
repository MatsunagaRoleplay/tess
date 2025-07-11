import os
import sys
from flask import Flask, render_template

# Ensure compatibility with different Python paths
sys.path.insert(0, os.path.dirname(__file__))

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Product data
PRODUCTS = [
    {
        'id': 1,
        'name': 'JASA PTERODACTYL',
        'description': 'Layanan lengkap untuk setup dan konfigurasi Pterodactyl Panel. Termasuk instalasi panel, Node.js, phpMyAdmin, dan theme custom.',
        'price': 'Rp10.000 - Rp20.000',
        'category': 'pterodactyl'
    },
    {
        'id': 2,
        'name': 'JASA SA:MP',
        'description': 'Layanan lengkap untuk server SA:MP mulai dari maintenance, bot UCP, mapping, hingga rename server untuk Basic Inferno dan LRP.',
        'price': 'Rp5.000 - Rp35.000',
        'category': 'samp'
    },
    {
        'id': 3,
        'name': 'JASA DISCORD',
        'description': 'Layanan lengkap untuk setup server Discord berbagai jenis: gaming, family, faction. Termasuk copy, remake, dan penambahan bot.',
        'price': 'Rp3.000 - Rp30.000',
        'category': 'discord'
    },
    {
        'id': 4,
        'name': 'SA:MP Hosting Budget',
        'description': 'Paket hosting SA:MP ekonomis mulai 15-100 slot | Singapore Server | Voice & .so/.dll Support | Unlimited RAM/CPU/Storage | Anti DDoS | Intel Xeon',
        'price': 'Rp15.000 - Rp95.000',
        'category': 'hosting'
    },
    {
        'id': 5,
        'name': 'SA:MP Hosting Ryzen',
        'description': 'Hosting premium dengan CPU Ryzen, SSD NVMe, bandwidth unlimited untuk performa maksimal',
        'price': 'COMING SOON',
        'category': 'hosting',
        'status': 'coming_soon'
    },
    {
        'id': 6,
        'name': 'BOT Hosting',
        'description': 'Hosting khusus untuk Discord bot, Telegram bot, dan aplikasi 24/7 dengan uptime tinggi',
        'price': 'COMING SOON',
        'category': 'hosting',
        'status': 'coming_soon'
    },
    {
        'id': 7,
        'name': 'VPS BASIC',
        'description': 'Virtual Private Server untuk kebutuhan dasar dengan harga terjangkau. 1GB RAM, 1 vCPU, 15GB SSD storage dengan full root access.',
        'price': 'COMING SOON',
        'category': 'vps',
        'status': 'coming_soon'
    },
    {
        'id': 8,
        'name': 'VPS KVM INDONESIA',
        'description': 'VPS KVM dengan server di Indonesia menggunakan Intel Xeon processor. 4 paket tersedia dari KVM 1 hingga KVM 4 dengan spesifikasi berbeda.',
        'price': 'Rp75.000 - Rp580.000',
        'category': 'vps'
    },
    {
        'id': 9,
        'name': 'VPS KVM SINGAPORE',
        'description': 'VPS KVM dengan server di Singapore untuk akses internasional. 2GB RAM, 1 vCPU, 30GB SSD dengan koneksi Asia-Pacific terbaik.',
        'price': 'COMING SOON',
        'category': 'vps',
        'status': 'coming_soon'
    },
    {
        'id': 10,
        'name': 'RDP BASIC',
        'description': 'Remote Desktop dengan spesifikasi dasar untuk kebutuhan standar. Windows Server 2019, 4GB RAM, 2 Core CPU dengan akses administrator.',
        'price': 'COMING SOON',
        'category': 'rdp',
        'status': 'coming_soon'
    },
    {
        'id': 11,
        'name': 'RDP MEDIUM',
        'description': 'Remote Desktop dengan spesifikasi menengah untuk performa lebih baik. Windows Server 2022, 8GB RAM, 4 Core CPU dengan software lengkap.',
        'price': 'COMING SOON',
        'category': 'rdp',
        'status': 'coming_soon'
    },
    {
        'id': 12,
        'name': 'RDP HIGH',
        'description': 'Remote Desktop dengan spesifikasi tinggi untuk performa maksimal. Windows Server 2022, 16GB RAM, 8 Core CPU dengan support premium.',
        'price': 'COMING SOON',
        'category': 'rdp',
        'status': 'coming_soon'
    }
]

CONTACT_INFO = {
    'whatsapp': '0882-2661-4281',
    'whatsapp_url': 'https://wa.me/6288226614281',
    'discord': 'vexcloud',
    'email': 'vexcloud01@email.com'
}

@app.route('/')
def index():
    featured_products = PRODUCTS[:3]  # Show first 3 products as featured
    return render_template('index.html', products=featured_products, contact=CONTACT_INFO)

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS, contact=CONTACT_INFO)

@app.route('/order')
def order():
    return render_template('order.html', contact=CONTACT_INFO)

@app.route('/contact')
def contact():
    return render_template('contact.html', contact=CONTACT_INFO)

@app.route('/samp-hosting')
def samp_hosting():
    return render_template('samp_hosting.html', contact=CONTACT_INFO)

@app.route('/katalog-pterodactyl')
def katalog_pterodactyl():
    return render_template('katalog_pterodactyl.html', contact=CONTACT_INFO)

@app.route('/katalog-samp')
def katalog_samp():
    return render_template('katalog_samp.html', contact=CONTACT_INFO)

@app.route('/katalog-discord')
def katalog_discord():
    return render_template('katalog_discord.html', contact=CONTACT_INFO)

@app.route('/katalog-vps-basic')
def katalog_vps_basic():
    return render_template('katalog_vps_basic.html', contact=CONTACT_INFO)

@app.route('/katalog-vps-kvm-indonesia')
def katalog_vps_kvm_indonesia():
    return render_template('katalog_vps_kvm_indonesia.html', contact=CONTACT_INFO)

@app.route('/katalog-vps-kvm-singapore')
def katalog_vps_kvm_singapore():
    return render_template('katalog_vps_kvm_singapore.html', contact=CONTACT_INFO)

@app.route('/katalog-rdp-basic')
def katalog_rdp_basic():
    return render_template('katalog_rdp_basic.html', contact=CONTACT_INFO)

@app.route('/katalog-rdp-medium')
def katalog_rdp_medium():
    return render_template('katalog_rdp_medium.html', contact=CONTACT_INFO)

@app.route('/katalog-rdp-high')
def katalog_rdp_high():
    return render_template('katalog_rdp_high.html', contact=CONTACT_INFO)

if __name__ == '__main__':
    # For development
    app.run(host='0.0.0.0', port=5000, debug=True)
    
# For production hosting (WSGI)
application = app
