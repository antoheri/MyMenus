import React from "react";
import { useNavigate } from "react-router-dom";
import { Container, Typography, Button, Box } from "@mui/material";

function Home() {
  const navigate = useNavigate();
  const goToReceipt = () => navigate("/receipt");
  return (
    <Container maxWidth="sm" style={{ textAlign: "center", padding: "20px" }}>
      <Typography variant="h2" component="h1" gutterBottom>
        Bienvenue sur <strong>My Menus</strong>
      </Typography>
      <Typography variant="body1" component="p">
        Ce projet a pour but de regrouper un grand nombre de plats afin d'en
        proposer aléatoirement aux utilisateurs lorsqu'ils cherchent quoi
        manger.
      </Typography>
      <br />
      <Typography variant="body1" component="p">
        Vous pouvez sélectionner le nombre de plats souhaité et créer une liste
        de favoris.
      </Typography>
      <Box display="flex" justifyContent="center" gap="20px" mt={4}>
        <Button variant="contained" color="primary" onClick={goToReceipt}>
          Découvrir une recette
        </Button>
        <Button variant="contained" color="secondary">
          Voir mes favoris
        </Button>
      </Box>
    </Container>
  );
}

export default Home;
