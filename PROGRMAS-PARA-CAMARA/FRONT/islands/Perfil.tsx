import { FunctionalComponent } from "preact";
import { card } from "../routes/perfil.tsx";
import { useState } from "preact/hooks";

type collection_card = {
  card: card[];
  collections: string[];
};

const Zona_usuario: FunctionalComponent<collection_card> = ({ card, collections }) => {

  const [name_collection, set_name_collection] = useState<string>("");

  const cartas_filtradas =
    name_collection === ""
      ? card
      : card.filter(
          (carta) => carta.coleccion === name_collection
        );

  return (
    <>
      <div>
        <h1>Zona de Usuario</h1>

        <h2>Colecciones</h2>

        <div>
          <button onClick={() => set_name_collection("")}>
            Todas
          </button>

          {collections.map((coleccion) => (
            <button
              type="button"
              key={coleccion}
              onClick={() => set_name_collection(coleccion)}
            >
              {coleccion}
            </button>
          ))}
        </div>

        <h2>Cartas</h2>

        <div>
          {cartas_filtradas.map((carta) => (
            <div key={carta.img}>
              <img src={carta.img} />
              <p>{carta.coleccion}</p>
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Zona_usuario;