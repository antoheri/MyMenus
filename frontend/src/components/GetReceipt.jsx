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

  useEffect(() => {
    fetchReceipt();
  }, [route, navigate]);

  return (
    <Container>
      <Card>
        <CardContent>
          <Typography variant="h3">Recette du jour</Typography>
          <Box>
            {receipt.map((r) => (
              <Box key={r.id} mb={2}>
                {r.entree && (
                  <Typography variant="body1">
                    <strong>Entrée:</strong> {r.entree}
                  </Typography>
                )}
                {r.plat_principal && (
                  <Typography variant="body1">
                    <strong>Plat principal:</strong> {r.plat_principal}
                  </Typography>
                )}
                {r.garniture && (
                  <Typography variant="body1">
                    <strong>Garniture:</strong> {r.garniture}
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
      <Button variant="contained" onClick={fetchReceipt}>
        {" "}
        Une autre ?
      </Button>
    </Container>
  );
}

export default Receipt;
