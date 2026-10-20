"use client"; // Le indica a Next.js que este componente interactúa en el navegador

import { useEffect, useState } from "react";

export default function Home() {
  const [mensajeBackend, setMensajeBackend] = useState("Cargando conexión...");

  useEffect(() => {
    // Hacemos la petición HTTP al puerto 8000
    fetch("http://127.0.0.1:8000/")
      .then((respuesta) => respuesta.json())
      .then((data) => {
        // Guardamos el mensaje que viene desde Python
        setMensajeBackend(data.estado);
      })
      .catch((error) => {
        console.error("Error conectando al backend:", error);
        setMensajeBackend("Error de conexión con FastAPI");
      });
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gray-900 text-white p-24">
      <div className="bg-gray-800 p-8 rounded-2xl shadow-xl text-center max-w-md w-full border border-gray-700">
        <h1 className="text-2xl font-bold mb-4 text-emerald-400">
          Plataforma de Sorteos
        </h1>
        <p className="text-gray-300 mb-6">Estado del servidor:</p>
        
        {/* Aquí mostramos el mensaje dinámico */}
        <div className="bg-gray-900 text-emerald-300 p-4 rounded-lg font-mono text-sm border border-emerald-900">
          {mensajeBackend}
        </div>
      </div>
    </main>
  );
}