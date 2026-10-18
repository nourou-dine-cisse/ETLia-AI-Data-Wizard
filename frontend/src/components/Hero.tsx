import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Animated gradient background */}
      <div className="absolute inset-0 bg-gradient-hero opacity-90 animate-gradient-shift bg-[length:200%_200%]" />

      {/* Subtle grid pattern */}
      <div
        className="absolute inset-0 opacity-10"
        style={{
          backgroundImage: `linear-gradient(hsl(var(--accent)) 1px, transparent 1px),
                           linear-gradient(90deg, hsl(var(--accent)) 1px, transparent 1px)`,
          backgroundSize: "50px 50px",
        }}
      />

      {/* Content */}
      <div className="relative z-10 max-w-5xl mx-auto px-6 text-center animate-fade-in">
        <div className="mb-8">
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
            Bienvenue à l'ère de <br />
            <span className="text-accent animate-float inline-block">
              l'ETL intelligente
            </span>
          </h1>
          <p className="text-xl md:text-2xl text-white/90 max-w-3xl mx-auto leading-relaxed">
            Je suis ETLIA, votre agent spécialisé dans l'automatisation des flux
            de données (Extraction, Transformation, Load). Transformez vos
            données en insights actionnables.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <Button
            size="lg"
            asChild
            className="bg-accent hover:bg-accent/90 text-white px-8 py-6 text-lg font-semibold rounded-lg shadow-glow transition-all duration-300 hover:scale-105 hover:shadow-xl group"
          >
            <a
              href="http://localhost:8501"
              target="_blank"
              rel="noopener noreferrer"
            >
              Essayez ETLIA
              <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
            </a>
          </Button>
          <Button
            size="lg"
            variant="outline"
            className="border-2 border-white text-white hover:bg-white hover:text-primary px-8 py-6 text-lg font-semibold rounded-lg backdrop-blur-sm transition-all duration-300"
          >
            En savoir plus
          </Button>
        </div>

        {/* Floating description */}
        <div className="mt-16 p-6 bg-white/10 backdrop-blur-md rounded-2xl border border-white/20 max-w-2xl mx-auto">
          <p className="text-white/95 text-lg leading-relaxed">
            Interagissez avec vos bases de données, automatisez vos ETL, générez
            des requêtes optimisées et obtenez des analyses claires tout avec
            quelques phrases.
          </p>
        </div>
      </div>

      {/* Bottom gradient fade */}
      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-background to-transparent" />
    </section>
  );
};

export default Hero;
