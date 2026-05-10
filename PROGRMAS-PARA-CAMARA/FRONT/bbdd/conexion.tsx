import { MongoClient, Collection, ObjectId } from "npm:mongodb@6.1.0";
import { card, collection_card } from "../routes/perfil.tsx";
export type card_bbdd = {
    _id?: ObjectId;
    name: string;
    img: string;
    coleccion?: string;
}
export const connectToMongoDB = async () => {
    const MONGO_URI = Deno.env.get("MONGO_URL");

    if (!MONGO_URI) {
    throw new Error("Falta la variable de entorno MONGO_URL");
    }

    const client = new MongoClient(MONGO_URI);
    await client.connect();

    const db = client.db("escaner_cartas");

    const translatorCollection: Collection<card_bbdd> = db.collection<card_bbdd>("cards");
    return translatorCollection;
};

export const get_collection_cards = async () => {
    const collection = await connectToMongoDB();
    return collection;
};

export const insert_card = async (card: card_bbdd) => {
    const collection = await get_collection_cards();
    await collection.insertOne(card);
}
export const get_unique_collections = async () => {
  const collection = await get_collection_cards();
  return await collection.distinct("coleccion");
}

export const get_all_cards = async () => {
  const collection = await get_collection_cards();
  const cartas:card[] = await collection.find().toArray();
  return cartas
}



