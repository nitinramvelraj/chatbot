import React from "react";

function SignInButton() {
  const handleSignIn = () => {
    // Implement the sign-in logic here
    console.log("Sign-in process initiated");
  };

  return <button onClick={handleSignIn}>Sign In</button>;
}

export default SignInButton;
