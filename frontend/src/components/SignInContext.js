import React, { createContext, useContext, useState } from "react";

// Create the context
const SignInContext = createContext();

// Create a provider component
export const SignInProvider = ({ children }) => {
  const [isSignedIn, setIsSignedIn] = useState(false);

  const signIn = () => setIsSignedIn(true);
  const signOut = () => setIsSignedIn(false);

  return (
    <SignInContext.Provider value={{ isSignedIn, signIn, signOut }}>
      {children}
    </SignInContext.Provider>
  );
};

// Custom hook to use the SignInContext
export const useSignIn = () => {
  const context = useContext(SignInContext);
  if (context === undefined) {
    throw new Error("useSignIn must be used within a SignInProvider");
  }
  return context;
};
