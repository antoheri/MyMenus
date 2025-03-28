import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import {
  CardContent,
  Typography,
  Button,
  Card,
  Container,
  Box,
} from "@mui/material";
import PropTypes from "prop-types";

function Receipt({ route }) {
  const [receipt, setReceipt] = useState([]);
  const navigate = useNavigate();

  const fetchReceipt = async () => {
    try {
      const response = await api.get(route);
      console.log(response.data);
      setReceipt(response.data);
      navigate("/receipt");
    } catch (error) {
      alert(error);
    }
  };

  const goToHome = () => navigate("/");

  useEffect(() => {
    fetchReceipt();
  }, [route, navigate]);

  return (
    <Container>
      <Card>
        <CardContent>
          <Typography variant="h3" mb={2}>
            Menu du jour
          </Typography>
          <Box>
            {receipt.map((r) => (
              <Box key={r.id}>
                {r.entree && (
                  <Typography variant="body1" mb={1}>
                    <strong>Entrée:</strong> {r.entree}
                  </Typography>
                )}
                {r.plat_principal && (
                  <Typography variant="body1" mb={1}>
                    <strong>Plat principal:</strong> {r.plat_principal}
                  </Typography>
                )}
                {r.garniture && (
                  <Typography variant="body1" mb={1}>
                    <strong>Garniture:</strong> {r.garniture}
                  </Typography>
                )}
                {r.produit_laitier_ou_divers && (
                  <Typography variant="body1" mb={1}>
                    <strong>Produit laitier ou divers:</strong>{" "}
                    {r.produit_laitier_ou_divers}
                  </Typography>
                )}
                {r.dessert && (
                  <Typography variant="body1">
                    <strong>Dessert:</strong> {r.dessert}
                  </Typography>
                )}
              </Box>
            ))}
          </Box>
        </CardContent>
      </Card>
      <Box mt={2} display="flex" justifyContent="center">
        <Box mr={2}>
          <Button variant="contained" onClick={fetchReceipt}>
            Une autre ?
          </Button>
        </Box>
        <Button variant="contained" color="secondary" onClick={goToHome}>
          Retour à l'accueil
        </Button>
      </Box>
    </Container>
  );
}
Receipt.propTypes = {
  route: PropTypes.string.isRequired,
};

export default Receipt;
