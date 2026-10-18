import { Button } from "@/components/ui/button";

const Navigation = () => {
  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-lg border-b border-border">
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          {/* Logo placeholder */}
          <div className="flex items-center gap-3">
            <img
              src="/favicon.ico"
              alt="ETLIA"
              className="w-20=2 h-20 rounded-lg"
            />
            <span className="text-2xl font-bold text-foreground">ETLIA</span>
          </div>

          {/* Navigation links */}
          <div className="hidden md:flex items-center gap-8">
            <button
              onClick={() => scrollToSection("hero")}
              className="text-foreground/80 hover:text-foreground transition-colors font-medium"
            >
              Accueil
            </button>
            <button
              onClick={() => scrollToSection("features")}
              className="text-foreground/80 hover:text-foreground transition-colors font-medium"
            >
              Fonctionnalités
            </button>
            <button
              onClick={() => scrollToSection("contact")}
              className="text-foreground/80 hover:text-foreground transition-colors font-medium"
            >
              Contact
            </button>
          </div>

          {/* CTA Button */}
          <Button
            asChild
            className="bg-primary hover:bg-primary/90 text-primary-foreground"
          >
            <a
              href="http://localhost:8501"
              target="_blank"
              rel="noopener noreferrer"
            >
              Essayer maintenant
            </a>
          </Button>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
