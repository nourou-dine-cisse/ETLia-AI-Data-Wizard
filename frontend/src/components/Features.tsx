import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Database, GitBranch, Zap, Shield } from "lucide-react";

const features = [
  {
    icon: Database,
    title: "Interaction avec vos données",
    description:
      "Connectez-vous à vos sources de données et explorez les à temps avec une interface intuitive et puissante.",
  },
  {
    icon: GitBranch,
    title: "Automatisation ETL",
    description:
      "Créez et orchestrez des pipelines ETL complexes avec une simplicité déconcertante grace à notre chatbot intégré. Extraction, transformation, chargement automatisés.",
  },
  {
    icon: Zap,
    title: "Analyse Intelligente",
    description:
      "Découvrez des insights cachés grâce à l'analyse automatique de vos flux de données et recevez des recommandations pertinentes.",
  },
  {
    icon: Shield,
    title: "Requêtes Sécurisées",
    description:
      "Générez des requêtes SQL optimisées et sécurisées automatiquement. Protection contre les injections et respect des bonnes pratiques.",
  },
];

const Features = () => {
  return (
    <section className="py-24 px-6 bg-background">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16 animate-fade-in">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
            Fonctionnalités clés
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Des outils puissants pour transformer votre façon de travailler avec
            les données
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <Card
                key={index}
                className="bg-gradient-card border-0 shadow-medium hover:shadow-glow transition-all duration-300 hover:-translate-y-2 group"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <CardHeader>
                  <div className="w-14 h-14 rounded-lg bg-primary/10 flex items-center justify-center mb-4 group-hover:bg-primary/20 transition-colors">
                    <Icon className="h-7 w-7 text-primary" />
                  </div>
                  <CardTitle className="text-xl font-bold text-foreground">
                    {feature.title}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-base leading-relaxed text-muted-foreground">
                    {feature.description}
                  </CardDescription>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Features;
