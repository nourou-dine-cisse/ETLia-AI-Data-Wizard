import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Mail, Calendar } from "lucide-react";

const Contact = () => {
  return (
    <section className="py-24 px-6 bg-muted/30">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12 animate-fade-in">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
            Prêt à transformer vos données ?
          </h2>
          <p className="text-accent animate-float inline-block">
            Contactez-nous ou planifiez une démonstration personnalisée
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Contact Form */}
          <Card className="bg-card shadow-medium border-0">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-2xl">
                <Mail className="h-6 w-6 text-primary" />
                Contactez-nous
              </CardTitle>
              <CardDescription>
                Remplissez le formulaire et notre équipe vous répondra
                rapidement
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <Input
                  placeholder="Votre nom"
                  className="bg-background border-border"
                />
              </div>
              <div>
                <Input
                  type="email"
                  placeholder="Votre email"
                  className="bg-background border-border"
                />
              </div>
              <div>
                <Textarea
                  placeholder="Votre message"
                  rows={4}
                  className="bg-background border-border resize-none"
                />
              </div>
              <Button className="w-full bg-primary hover:bg-primary/90 text-primary-foreground">
                Envoyer le message
              </Button>
            </CardContent>
          </Card>

          {/* Demo Request */}
          <Card className="bg-gradient-hero text-white shadow-glow border-0">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-2xl text-white">
                <Calendar className="h-6 w-6" />
                Planifier une démo
              </CardTitle>
              <CardDescription className="text-white/90">
                Découvrez ETLIA en action avec une démonstration personnalisée
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="space-y-4">
                <div className="flex items-start gap-3">
                  <div className="w-2 h-2 rounded-full bg-accent mt-2" />
                  <p className="text-white/95">
                    Démonstration complète des fonctionnalités
                  </p>
                </div>
                <div className="flex items-start gap-3">
                  <div className="w-2 h-2 rounded-full bg-accent mt-2" />
                  <p className="text-white/95">
                    Réponses à toutes vos questions
                  </p>
                </div>
                <div className="flex items-start gap-3">
                  <div className="w-2 h-2 rounded-full bg-accent mt-2" />
                  <p className="text-white/95">
                    Conseils personnalisés pour votre cas d'usage
                  </p>
                </div>
              </div>
              <Button
                className="w-full bg-accent hover:bg-accent/90 text-white shadow-lg hover:scale-105 transition-transform"
                size="lg"
              >
                Réserver une démo gratuite
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default Contact;
