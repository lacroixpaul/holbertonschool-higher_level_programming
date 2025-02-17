### Comparatif : HTTP vs HTTPS

| **Critère**           | **HTTP (HyperText Transfer Protocol)** | **HTTPS (HyperText Transfer Protocol Secure)** |
|----------------------|----------------------------------|-------------------------------------------|
| **Sécurité**        | ❌ Non sécurisé, données en clair | ✅ Sécurisé avec chiffrement SSL/TLS |
| **Chiffrement**     | ❌ Aucun, vulnérable aux attaques | ✅ Chiffrement des données en transit |
| **Authentification** | ❌ Pas de vérification de l’identité du serveur | ✅ Vérification du serveur via un certificat SSL/TLS |
| **Intégrité des données** | ❌ Données modifiables en transit | ✅ Protection contre l’altération des données |
| **Vulnérabilités**  | Exposé aux attaques MITM, écoute réseau, usurpation | Protégé contre MITM et interférences malveillantes |
| **Indicateur dans le navigateur** | 🚨 Affiché comme "Non sécurisé" | 🔒 Icône de cadenas, affiché comme "Sécurisé" |
| **Impact SEO**      | Moins bien référencé par Google | 🔥 Améliore le ranking SEO |
| **Utilisation**     | Sites non critiques (blogs, contenus statiques) | Sites nécessitant sécurité (e-commerce, API, connexion utilisateur) |
| **Port utilisé**    | 80 | 443 |
| **Coût**           | Gratuit (pas besoin de certificat) | Peut nécessiter l’achat d’un certificat SSL/TLS |
| **Exemple d’URL**   | `http://www.exemple.com` | `https://www.exemple.com` |

✅ **Conclusion** : HTTPS est indispensable pour garantir la **confidentialité**, l’**intégrité** et l’**authenticité** des données, surtout pour les sites manipulant des informations sensibles. 🚀
