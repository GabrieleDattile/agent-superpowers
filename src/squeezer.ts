/**
 * Token Squeezer for TypeScript / JavaScript
 * Author: Gabriele Dattile (https://github.com/GabrieleDattile)
 */

export interface CompressionResult {
  originalChars: number;
  compressedChars: number;
  savingsPercentage: number;
  compressedCode: string;
}

export function compressTypeScriptInterfaces(sourceCode: string): CompressionResult {
  const originalChars = sourceCode.length;

  // Strips multi-line and single-line comments, collapses whitespace
  const withoutComments = sourceCode
    .replace(/\/\*[\s\S]*?\*\//g, "")
    .replace(/\/\/.*/g, "");

  // Normalize excessive line breaks and whitespace
  const compressedCode = withoutComments
    .split("\n")
    .map((line) => line.trimEnd())
    .filter((line) => line.trim().length > 0)
    .join("\n");

  const compressedChars = compressedCode.length;
  const savingsPercentage = Math.max(0, Math.round((1 - compressedChars / originalChars) * 100));

  return {
    originalChars,
    compressedChars,
    savingsPercentage,
    compressedCode
  };
}
