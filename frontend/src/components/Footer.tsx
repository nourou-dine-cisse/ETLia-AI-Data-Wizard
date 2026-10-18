const Footer = () => {
  return (
    <footer className="bg-primary text-primary-foreground py-12 px-6">
      <div className="max-w-7xl mx-auto">
        <div className="grid md:grid-cols-3 gap-8 mb-8">
          <div>
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-lg bg-accent flex items-center justify-center font-bold text-white text-xl">
                <img src="/favicon.ico" alt="ETLIA" height={20} />
              </div>
              <span className="text-2xl font-bold">ETLIA</span>
            </div>
            <p className="text-primary-foreground/80">
              Votre agent intelligent pour l'analyse et l'automatisation des
              flux de données.
            </p>
          </div>

          <div>
            <h3 className="font-semibold text-lg mb-4">Liens rapides</h3>
            <ul className="space-y-2 text-primary-foreground/80">
              <li>
                <a
                  href="#hero"
                  className="hover:text-primary-foreground transition-colors"
                >
                  Accueil
                </a>
              </li>
              <li>
                <a
                  href="#features"
                  className="hover:text-primary-foreground transition-colors"
                >
                  Fonctionnalités
                </a>
              </li>
              <li>
                <a
                  href="#contact"
                  className="hover:text-primary-foreground transition-colors"
                >
                  Contact
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold text-lg mb-4">Contact</h3>
            <p className="text-primary-foreground/80">
              contact@etlia.com
              <br />
              +33 1 23 45 67 89
            </p>
          </div>
        </div>

        <div className="border-t border-primary-foreground/20 pt-8 text-center text-primary-foreground/80">
          <p>&copy; {new Date().getFullYear()} ETLIA. Tous droits réservés.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
